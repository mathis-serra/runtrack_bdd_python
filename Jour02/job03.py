import mysql.connector



mydb = mysql.connector.connect(
    host="localhost",
    user= "root",
    password="dominique59",
    database="Laplateforme"
)

cursor = mydb.cursor()



cursor.execute("INSERT INTO etage (nom_etage, numero_etage, superficie, VALUES ('RDC', 0, 500), ('R+1', 1, 500))");

cursor.execute("INSERT INTO salle (nom_salle, numero_etage, superficie, VALUES ('Lounge', 1, 100), ('Studio son', 1, 5) ('Broadcasting', 2, 50), ('Bocal Peda', 2, 4), ('Coworking', 2, 80), ('Studio Video', 2, 5))");



cursor.close()
mydb.close()
