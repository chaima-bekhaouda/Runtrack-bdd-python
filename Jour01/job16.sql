SELECT * FROM etudiant WHERE nom LIKE 'B%';

resultat:
+----+--------+-----------+-----+---------------------------------+
| id | nom    | prenom    | age | email                           |
+----+--------+-----------+-----+---------------------------------+
|  1 | Betty  | Spaghetti |  23 | betty.Spaghetti@laplateforme.io |
|  4 | Binkie | Barnes    |  16 | binkie.barnes@laplateforme.io   |
+----+--------+-----------+-----+---------------------------------+
2 rows in set (0.00 sec)