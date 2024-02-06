import mysql.connector

class Employe:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def create_employe(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, (nom, prenom, salaire, id_service))
        self.connection.commit()

    def read_employe(self):
        query = "SELECT * FROM employe"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update_employe(self, employe_id, new_salaire):
        query = "UPDATE employe SET salaire = %s WHERE id = %s"
        self.cursor.execute(query, (new_salaire, employe_id,))
        self.connection.commit()

    def delete_employe(self, employe_id):
        query = "DELETE FROM employe WHERE id = %s"
        self.cursor.execute(query, (employe_id,))
        self.connection.commit()

    def close_connection(self):
        self.connection.close()

# exemple d'utilisation
employe_manager = Employe(host='localhost', user='root', password=input("Quel est votre mot de passe : "), database='entreprise')

employe_manager.create_employe('Pichaut', 'Marie', 3000.00, 4)

employes = employe_manager.read_employe()

print("Liste des employés :\n")
for employe in employes:
    print(employe)

employe_manager.update_employe(1, 3000.00)

employes = employe_manager.read_employe()
print("\nListe des employés après mise à jour :\n")
for employe in employes:
    print(employe)

# id = 12 parce que j'ai crée plusieurs fois l'employe et comme l'id auto-increment
employe_manager.delete_employe(12)

employe_manager.update_employe(1, 2600.00)

# on revient à la liste de depart avec les valeurs de depart
employes = employe_manager.read_employe()
print("\nListe des employés après suppression :\n")
for employe in employes:
    print(employe)

employe_manager.close_connection()