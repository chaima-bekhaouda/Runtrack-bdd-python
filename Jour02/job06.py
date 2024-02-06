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

    # Calcul de la capacité totale des salles
    query_capacite = "SELECT SUM(capacite) FROM salle"
    cursor.execute(query_capacite)

    capacite_totale = cursor.fetchone()[0]

    if capacite_totale is not None:
        print(f"La capacité de toutes les salles est de : {capacite_totale}")
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