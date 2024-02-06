import mysql.connector

mdp = input("Quel est votre mot de passe : ")

config = {
    'user': 'root',
    'password': mdp,
    'host': 'localhost',
    'database': 'laplateforme',
}

try:
    connection = mysql.connector.connect(**config)

    cursor = connection.cursor()

    query = "SELECT * FROM etudiant"
    cursor.execute(query)

    students = cursor.fetchall()

    for student in students:
        print(student)

except mysql.connector.Error as err:
    print(f"Erreur: {err}")

finally:
    if 'cursor' in locals() and cursor is not None:
        cursor.close()

    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Connexion à la base de données fermée.")