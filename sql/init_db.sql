Create database csc468;
Use csc468;
Create table if not exist cattle
(name VARCHAR(255), breed VARCHAR(255), color VARCHAR(255));
LOAD data INFILE var/lib/mysql-files/ani.csv into table cattle;
