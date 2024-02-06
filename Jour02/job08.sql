CREATE DATABASE zoo;
Query OK, 1 row affected (0.01 sec)

USE zoo;
Database changed

CREATE TABLE animal (
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     nom VARCHAR(255) NOT NULL,
    ->     race VARCHAR(255) NOT NULL,
    ->     cage_id INT,
    ->     date_naissance DATE,
    ->     pays_origine VARCHAR(255)
    -> );
Query OK, 0 rows affected (0.03 sec)

CREATE TABLE cage (
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     superficie FLOAT NOT NULL,
    ->     capacite_max INT NOT NULL
    -> );
Query OK, 0 rows affected (0.03 sec)