import mysql.connector



mydb = mysql.connector.connect(
    host="localhost",
    user= "root",
    password="dominique59",
    database="Laplateforme"
)

cursor = mydb.cursor()

# Exécution de la requête pour calculer la superficie totale des étages
requete_sql = "SELECT SUM(superficie) AS superficie_totale FROM etage"
cursor.execute(requete_sql)

# Récupération du résultat
resultat = cursor.fetchone()
superficie_totale = resultat[0]

# Affichage du résultat
print(f"La superficie de La Plateforme est de {superficie_totale} m2")

# Fermeture du curseur et de la connexion
cursor.close()
mydb.close()