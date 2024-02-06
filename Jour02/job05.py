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

    query_superficie = "SELECT SUM(superficie) FROM etage"
    cursor.execute(query_superficie)

    superficie_totale = cursor.fetchone()[0]

    if superficie_totale is not None:
        print(f"La superficie de La Plateforme est de {superficie_totale} m2")
    else:
        print("Aucune donnée trouvée.")

except mysql.connector.Error as err:
    print(f"Erreur: {err}")

finally:
    if 'cursor' in locals() and cursor is not None:
        cursor.close()

    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Connexion à la base de données fermée.")