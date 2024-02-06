UPDATE etudiant
    -> SET age = '20'
    -> WHERE  id = 1;

resultat:
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

SELECT * FROM etudiant WHERE id = 1;

resultat:
+----+-------+-----------+-----+---------------------------------+
| id | nom   | prenom    | age | email                           |
+----+-------+-----------+-----+---------------------------------+
|  1 | Betty | Spaghetti |  20 | betty.Spaghetti@laplateforme.io |
+----+-------+-----------+-----+---------------------------------+
1 row in set (0.00 sec)
