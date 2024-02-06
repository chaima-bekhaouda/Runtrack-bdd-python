CREATE TABLE IF NOT EXITS employe (
    ->     id INT PRIMARY KEY AUTO_INCREMENT,
    ->     nom VARCHAR(255),
    ->     prenom VARCHAR(255),
    ->     salaire DECIMAL(10, 2),
    ->     id_service INT
    -> );
Query OK, 0 rows affected (0.05 sec)

resultat:
+----------------------+
| Tables_in_entreprise |
+----------------------+
| employe              |
+----------------------+
1 row in set (0.00 sec)

INSERT INTO employe (nom, prenom, salaire, id_service) VALUES
    -> ('Betty', 'Spaghetti', 2600.00, 5),
    -> ('Chuck', 'Steak', 2800.75, 1),
    -> ('Doe', 'John', 3200.00, 3),
    -> ('Binkie', 'Barnes', 3000.00, 4),
    -> ('Dupuis', 'Gertrude', 3500.00, 2);
Query OK, 5 rows affected (0.01 sec)
Records: 5  Duplicates: 0  Warnings: 0

SELECT * FROM employe;

resultat:
+----+--------+-----------+---------+------------+
| id | nom    | prenom    | salaire | id_service |
+----+--------+-----------+---------+------------+
|  1 | Betty  | Spaghetti | 2600.00 |          5 |
|  2 | Chuck  | Steak     | 2800.75 |          1 |
|  3 | Doe    | John      | 3200.00 |          3 |
|  4 | Binkie | Barnes    | 3000.00 |          4 |
|  5 | Dupuis | Gertrude  | 3500.00 |          2 |
+----+--------+-----------+---------+------------+
5 rows in set (0.00 sec)


SELECT * FROM employe WHERE salaire > 3000;

resultat:
+----+--------+----------+---------+------------+
| id | nom    | prenom   | salaire | id_service |
+----+--------+----------+---------+------------+
|  3 | Doe    | John     | 3200.00 |          3 |
|  5 | Dupuis | Gertrude | 3500.00 |          2 |
+----+--------+----------+---------+------------+
2 rows in set (0.00 sec)

CREATE TABLE IF NOT EXISTS service (
    ->     id INT PRIMARY KEY AUTO_INCREMENT,
    ->     nom VARCHAR(255)
    -> );
Query OK, 0 rows affected (0.06 sec)

INSERT INTO service (nom) VALUES
    -> ('Comptabilité'),
    -> ('Marketing'),
    -> ('Développement'),
    -> ('Ressources humaines'),
    -> ('Support technique');
Query OK, 5 rows affected (0.01 sec)
Records: 5  Duplicates: 0  Warnings: 0

SELECT * FROM service;

resultat:
+----+---------------------+
| id | nom                 |
+----+---------------------+
|  1 | Comptabilité        |
|  2 | Marketing           |
|  3 | Développement       |
|  4 | Ressources humaines |
|  5 | Support technique   |
+----+---------------------+
5 rows in set (0.00 sec)

 SELECT employe.*, service.nom AS service_nom
    -> FROM employe
    -> JOIN service ON employe.id_service = service.id;

resultat:
+----+--------+-----------+---------+------------+---------------------+
| id | nom    | prenom    | salaire | id_service | service_nom         |
+----+--------+-----------+---------+------------+---------------------+
|  1 | Betty  | Spaghetti | 2600.00 |          5 | Support technique   |
|  2 | Chuck  | Steak     | 2800.75 |          1 | Comptabilité        |
|  3 | Doe    | John      | 3200.00 |          3 | Développement       |
|  4 | Binkie | Barnes    | 3000.00 |          4 | Ressources humaines |
|  5 | Dupuis | Gertrude  | 3500.00 |          2 | Marketing           |
+----+--------+-----------+---------+------------+---------------------+
5 rows in set (0.00 sec)
