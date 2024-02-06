SELECT * FROM etudiant WHERE id = '5';
SELECT * FROM etudiant WHERE nom = 'Dupuis';
SELECT * FROM etudiant WHERE prenom = 'Gertrude';
SELECT * FROM etudiant WHERE email = 'gertrude.dupuis@laplateforme.io';
SELECT * FROM etudiant WHERE age = 'age';

resultat:
+----+--------+----------+-----+---------------------------------+
| id | nom    | prenom   | age | email                           |
+----+--------+----------+-----+---------------------------------+
|  5 | Dupuis | Gertrude |  20 | gertrude.dupuis@laplateforme.io |
+----+--------+----------+-----+---------------------------------+
1 row in set (0.00 sec)
