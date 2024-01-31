import mysql.connector

class EmployeManager:
    def __init__(self):
        self.connexion = mysql.connector.connect(
            host="localhost",
            user= "root",
            password="dominique59",
            database="emtrise"
        )
        self.curseur = self.connexion.cursor()

    def inserer_employe(self, nom, prenom, salaire, id_service):
        sql = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        valeurs = (nom, prenom, salaire, id_service)
        self.curseur.execute(sql, valeurs)
        self.connexion.commit()

    def recuperer_employes_salaire_superieur_a(self, seuil_salaire):
        sql = "SELECT * FROM employe WHERE salaire > %s"
        self.curseur.execute(sql, (seuil_salaire,))
        resultats = self.curseur.fetchall()
        return resultats

    def recuperer_employes_et_services(self):
        sql = "SELECT employe.*, service.nom AS nom_service FROM employe JOIN service ON employe.id_service = service.id"
        self.curseur.execute(sql)
        resultats = self.curseur.fetchall()
        return resultats

    def fermer_connexion(self):
        self.curseur.close()
        self.connexion.close()

# Exemple d'utilisation
employe_manager = EmployeManager()
employe_manager.inserer_employe('Nom5', 'Prenom5', 3800.00, 2)
employes_salaire_superieur_3000 = employe_manager.recuperer_employes_salaire_superieur_a(3000)
employes_et_services = employe_manager.recuperer_employes_et_services()

for employe in employes_salaire_superieur_3000:
    print(employe)

for employe_service in employes_et_services:
    print(employe_service)

employe_manager.fermer_connexion()
