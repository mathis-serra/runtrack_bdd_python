import mysql.connector



mydb = mysql.connector.connect(
    host="localhost",
    user= "root",
    password="dominique59",
    database="Laplateforme"
)

cursor = mydb.cursor()

cursor.execute(
    "CREATE TABLE etage (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), numero INT, superficie INT)"
);

cursor.execute(
    "CREATE TABLE salle (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), id_etage INT, capacite INT,)"
);

