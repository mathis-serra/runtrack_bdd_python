import mysql.connector

class zoo_manager():
    def __init__(self, user, password, host, database):
        self.cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)
        self.cursor = self.cnx.cursor()

    def add_animal(self, nom, race, id_cage, date_naissance, pays_origine):
        exec_ani = f"INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES ('{nom}','{race}',{id_cage},'{date_naissance}','{pays_origine}')"
        self.cursor.execute(exec_ani)
        self.cnx.commit()

    def add_cage(self, superficie,capacite_max):
        exec_cage = f"INSERT INTO cage (superficie,capacite_max) VALUES ({superficie},{capacite_max})"
        self.cursor.execute(exec_cage)
        self.cnx.commit()

    def del_animal(self,id_ani):
        exec_ani_del = f"DELETE FROM animal WHERE id = {id_ani}"
        self.cursor.execute(exec_ani_del)
        self.cnx.commit()

    def del_cage(self,id_cage):
        exec_cage_del = f"DELETE FROM cage WHERE id = {id_cage}"
        self.cursor.execute(exec_cage_del)
        self.cnx.commit()

    def update_ani(self,id_ani,what,change):
        exec_ani_upd=f"UPDATE animal SET {what} = {change} WHERE id = {id_ani}"
        self.cursor.execute(exec_ani_upd)
        self.cnx.commit()

    def update_cage(self,id_cage,what,change):
        exec_cage_upd=f"UPDATE cage SET {what} = {change} WHERE id = {id_cage}"
        self.cursor.execute(exec_cage_upd)
        self.cnx.commit()

    def read_all_animals(self):
        self.cursor.execute("SELECT * FROM animal")
        return self.cursor.fetchall()
    
    def read_all_cages(self):
        self.cursor.execute("SELECT * FROM cage")
        return self.cursor.fetchall()
    
    def read_animals_id(self, id_animal):
        exec_read_id_ani = f"SELECT * FROM animal WHERE id = {id_animal}"
        self.cursor.execute(exec_read_id_ani)
        return self.cursor.fetchone()
    
    def read_cages_id(self, id_cages):
        exec_read_id_cages = f"SELECT * FROM cage WHERE id = {id_cages}"
        self.cursor.execute(exec_read_id_cages)
        return self.cursor.fetchone()
    
    def superficie_cage(self):
        self.cursor.execute("SELECT SUM(superficie) FROM cage")
        total_superficie = self.cursor.fetchone()[0]
        print(f"La superficie totale de toutes les cages est de {total_superficie} m2")

    def close(self):
        self.cursor.close()
        self.cnx.close()


mon_zoo=zoo_manager('root',"n21217916","localhost","zoo")
mon_zoo.add_cage(50,5)
mon_zoo.add_animal("Lion","Félin",1,"2010-05-01","Afrique")
mon_zoo.add_animal("Pigeon","Oiseaux",1,"2013-01-10","France")
print(mon_zoo.read_all_animals())
print(mon_zoo.read_all_cages())
mon_zoo.del_animal(2)
mon_zoo.superficie_cage()
mon_zoo.close()
