import mysql.connector



mydb = mysql.connector.connect(
    host="localhost",
    user= "root",
    password="dominique59",
    database="Laplateforme"
)

cursor = mydb.cursor()

# Exécution de la requête pour récupérer les noms et les capacités
requete_sql = "SELECT nom, capacite FROM salle"
cursor.execute(requete_sql)

# Récupération des résultats
resultats = cursor.fetchall()

# Affichage des résultats
for resultat in resultats:
    nom, capacite = resultat
    print(f"Nom: {nom}, Capacité: {capacite}")

# Fermeture du curseur et de la connexion
cursor.close()
mydb.close()