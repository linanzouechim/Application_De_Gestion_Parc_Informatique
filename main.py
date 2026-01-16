# Programme utiliser sqlite et PyQt6
# Importer les packages necessaires

import sqlite3

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QLabel, \
    QMessageBox


def popup_warning(titre, message):
    QMessageBox.warning(fen, titre, message)


def CreerTable():
    print("créer la table")
    conn = sqlite3.connect("projet2.db")
    cursor = conn.cursor()
    # requette ici
    cursor.execute(
        "CREATE TABLE if not exists Poste(PosteID_Mac varchar(255) PRIMARY KEY,Nom_Poste varchar(255),Departement varchar(255),Utilisateur varchar(255),Systeme varchar(255),IP varchar(255) ,Etat varchar(255));")
    conn.commit()


def InsererDansTablePoste():
    print("inser dans la table")

    conn = sqlite3.connect("projet2.db")
    cursor = conn.cursor()
    # requette ici
    try:
        print("INSERT INTO Poste VALUES ('" + lineEditID_Poste_MacA.text() + "','" + lineEditNom_Poste.text() + "','" + lineEditDepartement.text() + "','" + lineEditUtilisateur.text() + "','" + lineEditSysteme.text() + "','" + lineEditIP.text() + "','" + lineEditEtat.text() + "');")
        cursor.execute(
            "INSERT INTO Poste VALUES ('" + lineEditID_Poste_MacA.text() + "','" + lineEditNom_Poste.text()  + "','" + lineEditDepartement.text() + "','" + lineEditUtilisateur.text() + "','" + lineEditSysteme.text() +  "','" + lineEditIP.text()  +"','" + lineEditEtat.text() + "');")
    except Exception as e:
        print("L'ID doit être un entier pas encore enregistré")
        popup_warning("Attention", "Mac Address déja enregistrée")

    conn.commit()
    AfficherTout()


def SupprimerId():
    print("supprimer dans la table")
    conn = sqlite3.connect("projet2.db")
    cursor = conn.cursor()
    # requette ici

    if selected_column == "0" :
        cursor.execute("DELETE FROM Poste WHERE PosteID_Mac= '" + id + "';")
    else :
        print("Bien vouloir sélectionner l'ID du contact à supprimer")
        popup_warning("Attention", "Bien vouloir sélectionner l'Adresse Mac du poste à supprimer.")

    conn.commit()
    AfficherTout()


def AfficherTout():
    print("afficher toute la table")
    conn = sqlite3.connect("projet2.db")
    cursor = conn.cursor()
    # requette ici
    cursor.execute("SELECT * FROM Poste")
    resultat = cursor.fetchall()

    # QTable
    qtab.setRowCount(len(resultat))
    qtab.setColumnCount(7)
    qtab.setGeometry(50, 250, 750, 200)
    qtab.setHorizontalHeaderLabels(['Mac Address', 'Nom', 'Département', 'Utilisateur', 'Systeme', 'Etat', 'IP'])
    #
    for i in range(len(resultat)):
        for j in range(7):
            qtab.setItem(i, j, QTableWidgetItem(str(resultat[i][j])))


def ModifierTable():
    global selected_row
    if selected_row < 0:
        print("Aucune ligne sélectionnée")
        return

    # Afficher le NOUVEAU texte (ex : la colonne Nom)
    print("Modifier la table")
    newNom_Poste = qtab.item(selected_row, 1).text()
    print("Nouveau Nom:", qtab.item(selected_row, 1).text())
    newDepartement = qtab.item(selected_row, 2).text()
    print("Nouveau Prenom:", qtab.item(selected_row, 2).text())
    newUtilisateur = qtab.item(selected_row, 3).text()
    newSysteme = qtab.item(selected_row, 4).text()
    newIP = qtab.item(selected_row, 5).text()
    newEtat = qtab.item(selected_row, 6).text()
    SelectID = qtab.item(selected_row, 0).text()

    conn = sqlite3.connect("projet2.db")
    cursor = conn.cursor()
    print("Select ID:" + SelectID)
    print(
        "UPDATE Poste SET Nom_Poste='" + newNom_Poste + "', Departement='" + newDepartement + "', Utilisateur='" + newUtilisateur + "', Systeme='" + newSysteme +"', IP='" + newIP +"', Etat='" + newEtat +"'  WHERE PosteID_Mac= '" + SelectID + "';")
    cursor.execute(
        "UPDATE Poste SET Nom_Poste='" + newNom_Poste + "', Departement='" + newDepartement + "', Utilisateur='" + newUtilisateur + "', Systeme='" + newSysteme +"', IP='" + newIP +"', Etat='" + newEtat +"'  WHERE PosteID_Mac='" + SelectID + "';")
#        "CREATE TABLE if not exists Poste(PosteID_Mac int PRIMARY KEY,Nom_Poste varchar(255),Departement varchar(255),Utilisateur varchar(255),Systeme varchar(255),IP varchar(255) ,Etat varchar(255),);")

    print("Nouveau Nom:" + newNom_Poste)
    conn.commit()
    print("Nouveau Nom:" + newNom_Poste)
    AfficherTout()


# 1-fenetre
app = QApplication([])
fen = QWidget()
fen.setWindowTitle("Parc informatique")
fen.setGeometry(100, 100, 950, 500)
fen.setStyleSheet("""
    QWidget {
        background: qlineargradient(
            x1:0, y1:0, x2:0, y2:1,
            stop:0 #d4f5e3,
            stop:1 #b8ebd1
        );
    }
""")
CreerTable()

labelTitre = QLabel("/****/     Parc Informatique      /****/", fen)
labelTitre.setGeometry(0, 0, 950, 50)  # largeur de la fenêtre, hauteur du bandeau
labelTitre.setAlignment(Qt.AlignmentFlag.AlignCenter)

labelTitre.setStyleSheet("""
    background-color: #2ecc71;   /* vert doux */
    color: white;
    font-size: 22px;
    font-weight: bold;
    border-bottom: 2px solid #27ae60;
""")

# 2- Créer un boutton créer la table
# btn1 = QPushButton(fen)
# btn1.setText("Créer Table")
# btn1.setGeometry(500, 100, 100, 30)
# btn1.clicked.connect(CreerTable)

# 2- Créer un boutton inserer
btn2 = QPushButton(fen)
btn2.setText("Inserer")
btn2.setGeometry(800, 150, 100, 30)
btn2.setStyleSheet("""

    font-weight: bold;
    font-size: 12px;
    background-color: #a8e6c8;
    padding: 4px;
    border: 1px solid #7fcfa9;

""")
btn2.clicked.connect(InsererDansTablePoste)

# 2- Créer des champs pour le btn inserer
lineEditID_Poste_MacA = QLineEdit(fen)
lineEditID_Poste_MacA.setGeometry(50, 150, 100, 30)
lineEditNom_Poste = QLineEdit(fen)
lineEditNom_Poste.setGeometry(150, 150, 100, 30)
lineEditDepartement = QLineEdit(fen)
lineEditDepartement.setGeometry(250, 150, 100, 30)
lineEditUtilisateur = QLineEdit(fen)
lineEditUtilisateur.setGeometry(350, 150, 100, 30)
lineEditSysteme = QLineEdit(fen)
lineEditSysteme.setGeometry(450, 150, 100, 30)
lineEditIP = QLineEdit(fen)
lineEditIP.setGeometry(550, 150, 100, 30)
lineEditEtat = QLineEdit(fen)
lineEditEtat.setGeometry(650, 150, 100, 30)

# 2- Créer un boutton AfficherTout
# btn3 = QPushButton(fen)
# btn3.setText("AfficherTout")
# btn3.setGeometry(500, 250, 100, 30)
# btn3.clicked.connect(AfficherTout)


# 2- Créer un boutton modifier la table
btn5 = QPushButton(fen)
btn5.setText("Modifier")
btn5.setGeometry(800, 250, 100, 30)
btn5.setStyleSheet("""

    font-weight: bold;
    font-size: 12px;
    background-color: #a8e6c8;
    padding: 4px;
    border: 1px solid #7fcfa9;

""")
btn5.clicked.connect(ModifierTable)

# QTable
qtab = QTableWidget(fen)
qtab.setRowCount(7)
qtab.setColumnCount(7)
qtab.setGeometry(50, 250, 750, 200)
qtab.setStyleSheet("""
    QHeaderView::section {
        font-weight: bold;
        font-size: 12px;
        background-color: #a8e6c8;
        padding: 4px;
        border: 1px solid #7fcfa9;
    }
""")
qtab.setHorizontalHeaderLabels(['Mac Address', 'Nom', 'Département', 'Utilisateur', 'Systeme', 'Etat', 'IP'])

selected_row = -1


def getClickedCell(row, column):
    print('clicked!', row, column)
    print(qtab.item(row, column).text())
    global selected_row
    selected_row = row
    global selected_column
    selected_column = str(column)
    print("colone"+ selected_column)
    global id
    id = str(qtab.item(row, column).text())
    print("Valeur cellule" + str(qtab.item(row, column).text()))

#lineEditSuppID = QLineEdit(fen)


qtab.cellClicked.connect(getClickedCell)

#
# 2- Créer un boutton supprimer
btn4 = QPushButton(fen)
btn4.setText("Supprimer")
btn4.setGeometry(800, 200, 100, 30)
btn4.setStyleSheet("""

    font-weight: bold;
    font-size: 12px;
    background-color: #a8e6c8;
    padding: 4px;
    border: 1px solid #7fcfa9;

""")
btn4.clicked.connect(SupprimerId)

# lineEditSuppID = QLineEdit(fen)
# lineEditSuppID.setGeometry(350, 200, 100, 30)

AfficherTout()
fen.show()
app.exec()