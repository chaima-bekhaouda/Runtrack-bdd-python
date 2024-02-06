DELETE FROM etudiant
    -> WHERE id = 3;

resultat:
Query OK, 1 row affected (0.01 sec)

SELECT * FROM etudiant;

resultat:
+----+--------+-----------+-----+---------------------------------+
| id | nom    | prenom    | age | email                           |
+----+--------+-----------+-----+---------------------------------+
|  1 | Betty  | Spaghetti |  20 | betty.Spaghetti@laplateforme.io |
|  2 | Chuck  | Steak     |  45 | chuck.steak@laplateforme.io     |
|  4 | Binkie | Barnes    |  16 | binkie.barnes@laplateforme.io   |
|  5 | Dupuis | Gertrude  |  20 | gertrude.dupuis@laplateforme.io |
|  6 | Dupuis | Martin    |  18 | martin.dupuis@laplateforme.io   |
+----+--------+-----------+-----+---------------------------------+
5 rows in set (0.00 sec)
