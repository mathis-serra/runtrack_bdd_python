import mysql.connector



mydb = mysql.connector.connect(
    host="localhost",
    user= "root",
    password="dominique59",
    database="Laplateforme"
)

cursor = mydb.cursor()


# Exécution de la requête pour calculer la capacité totale des salles
requete_sql = "SELECT SUM(capacite) AS capacite_totale FROM salle"
cursor.execute(requete_sql)

# Récupération du résultat
resultat = cursor.fetchone()
capacite_totale = resultat[0]

# Affichage du résultat
print(f"La capacité totale des salles est de {capacite_totale} personnes")

# Fermeture du curseur et de la connexion
cursor.close()
mydb.close()