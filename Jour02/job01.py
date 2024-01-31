import mysql.connector



mydb = mysql.connector.connect(
    host="localhost",
    user= "root",
    password="dominique59",
    database="Laplateforme"
)

cursor = mydb.cursor()


cursor.execute("SELECT * FROM etudiant")

result = cursor.fetchall()

results = cursor.fetchone()
print(results)


cursor.close()
mydb.close()