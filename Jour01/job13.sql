SELECT * FROM etudiant WHERE age > '17' AND age < '26';

resultat :
+----+--------+-----------+-----+---------------------------------+
| id | nom    | prenom    | age | email                           |
+----+--------+-----------+-----+---------------------------------+
|  1 | Betty  | Spaghetti |  23 | betty.Spaghetti@laplateforme.io |
|  3 | Doe    | John      |  18 | john.doe@laplateforme.io        |
|  5 | Dupuis | Gertrude  |  20 | gertrude.dupuis@laplateforme.io |
|  6 | Dupuis | Martin    |  18 | martin.dupuis@laplateforme.io   |
+----+--------+-----------+-----+---------------------------------+
4 rows in set (0.00 sec)