import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=input("Quel est votre mot de passe : "),
    database="zoo"
)
cursor = conn.cursor()

def ajouter_animal(nom, race, cage_id, date_naissance, pays_origine):
    cursor.execute('''
        INSERT INTO animal (nom, race, cage_id, date_naissance, pays_origine)
        VALUES (%s, %s, %s, %s, %s)
    ''', (nom, race, cage_id, date_naissance, pays_origine))
    conn.commit()

def ajouter_cage(superficie, capacite_max):
    cursor.execute('''
        INSERT INTO cage (superficie, capacite_max)
        VALUES (%s, %s)
    ''', (superficie, capacite_max))
    conn.commit()

def update_animal(value, modified_value, animal_id):
        req = f"UPDATE animal SET {value} = %s WHERE id = %s"
        cursor.execute(req, (modified_value, animal_id))
        conn.commit()

def update_cage(value, modified_value, cage_id):
        req = f"UPDATE cage SET {value} = %s WHERE id = %s"
        cursor.execute(req, (modified_value, cage_id))
        conn.commit()

def delete_animal(animal_id):
    cursor.execute('''
                   DELETE FROM animal WHERE id = %s
                   ''', (animal_id,))
    conn.commit()

def delete_cage(cage_id):
    cursor.execute('''
                   DELETE FROM cage WHERE id = %s
                   ''', (cage_id,))
    conn.commit()

def afficher_animaux():
    cursor.execute('''
        SELECT * FROM animal
    ''')
    animaux = cursor.fetchall()
    for animal in animaux:
        print(animal)


def animaux_dans_cages():
    cursor.execute('''
        SELECT cage.id, cage.superficie, animal.nom, animal.race
        FROM cage
        LEFT JOIN animal ON cage.id = animal.cage_id
    ''')
    animaux_cages = cursor.fetchall()
    for animal_cage in animaux_cages:
        print(animal_cage)

def superficie_totale():
    cursor.execute('''
        SELECT SUM(superficie) FROM cage
    ''')
    superficie = cursor.fetchone()[0]
    return superficie

while True:
    print("\n1. Ajouter un animal")
    print("2. Ajouter une cage")
    print("3. Afficher tous les animaux")
    print("4. Afficher les animaux dans les cages")
    print("5. Calculer la superficie totale des cages")
    print("6. Modifier")
    print("7. Supprimer")
    print("8. Quitter")

    choix = input("Choisissez une option : ")

    if choix == '1':
        nom = input("Nom de l'animal : ")
        race = input("Race de l'animal : ")
        cage_id = input("Numero de la cage : ")
        date_naissance = input("Date de naissance : ")
        pays_origine = input("Pays d'origine : ")
        ajouter_animal(nom, race, cage_id, date_naissance, pays_origine)

    elif choix == '2':
        superficie = float(input("Superficie de la cage : "))
        capacite_max = int(input("Capacité maximale de la cage : "))
        ajouter_cage(superficie, capacite_max)

    elif choix == '3':
        afficher_animaux()

    elif choix == '4':
        animaux_dans_cages()

    elif choix == '5':
        print(f"Superficie totale des cages : {superficie_totale()} m²")

    elif choix == '6':
        while True:
            print("\n1. Modifier un animal")
            print("2. Modifier une cage")
            print("3. Quitter")

            choix = input("Choisissez une option : ")

            if choix == '1':
                while True:
                    print("\n1. Modifier le nom de l'animal")
                    print("2. Modifier la race de l'animal")
                    print("3. Modifier le numero de la cage de l'animal")
                    print("4. Modifier la date de naissance de l'animal")
                    print("5. Modifier le pays d'origine de l'animal")
                    print("6. Quitter")

                    choix = input("Choisissez une option : ")
                    if choix == '1':

                        animal_id = input("Veuillez saisir l'id de l'animal : ")
                        new_name = input("Veuillez saisir le nouveau nom de l'animal : ")
                        update_animal('nom',new_name, animal_id )

                    elif choix == '2':

                        animal_id = input("Veuillez saisir l'id de l'animal : ")
                        new_race = input("Veuillez saisir la nouvelle race de l'animal : ")
                        update_animal('race',new_race, animal_id )

                    elif choix == '3':

                        animal_id = input("Veuillez saisir l'id de l'animal : ")
                        new_cage_id = input("Veuillez saisir le nouveau id de la cage de l'animal : ")
                        update_animal('cage_id',new_date, animal_id )

                    elif choix == '4':

                        animal_id = input("Veuillez saisir l'id de l'animal : ")
                        new_date = input("Veuillez saisir la nouvelle date de naissance de l'animal : ")
                        update_animal('date_naissance',new_date, animal_id )

                    elif choix == '5':

                        animal_id = input("Veuillez saisir l'id de l'animal : ")
                        new_country = input("Veuillez saisir le nouveau pays d'origine de l'animal : ")
                        update_animal('pays_origine',new_country, animal_id )

                    elif choix =='6':
                        break
                    else:
                         print("Option invalide. Veuillez choisir une option valide.")

            elif choix == '2':
                while True:
                    print("\n1. Modifier la superficie de la cage")
                    print("2. Modifier la capacité maximum de la cage")
                    print("3. Quitter")

                    choix = input("Choisissez une option : ")
                    if choix == '1':

                        cage_id = input("Veuillez saisir l'id de la cage : ")
                        new_area = input("Veuillez saisir la nouvelle superficie de la cage : ")
                        update_cage("superficie", new_area, cage_id)

                    elif choix == '2':

                        cage_id = input("Veuillez saisir l'id de l'animal : ")
                        new_capacity = input("Veuillez saisir la nouvelle capacité de la cage : ")
                        update_cage("capacite_max", new_capacity, cage_id)

                    elif choix == '3':
                        break
                    else:
                        print("Option invalide. Veuillez choisir une option valide.")
            elif choix == '3':
                break
            else:
                print("Option invalide. Veuillez choisir une option valide.")

    elif choix == '7':
        while True:
            print("\n1. Supprimer un animal")
            print("2. Supprimer une cage")
            print("3. Quitter")

            choix = input("Choisissez une option : ")
            if choix == '1':

                animal_id = input("Veuillez saisir l'id de l'animal :")
                delete_animal(animal_id)

            elif choix == '2':

                cage_id = input("Veuillez saisir l'id de la cage : ")
                delete_cage(cage_id)

            elif choix == '3':
                break
            else:
                print("Option invalide. Veuillez choisir une option valide.")
    elif choix == '8':
        break
    else:
        print("Option invalide. Veuillez choisir une option valide.")

conn.close()