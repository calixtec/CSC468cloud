CREATE database csc468;
USE csc468;

CREATE table cattle (
name VARCHAR(255),
breed VARCHAR(255),
color VARCHAR(255)
);

LOAD DATA INFILE  '/var/lib/mysql-files/cattle.csv'
INTO TABLE cattle
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
