-- We are all unique!
-- SQL script that creates a table
CREATE TABLE IF NOT EXISTS users (
       id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
       email varchar(255) NOT NULL UNIQUE,
       NAME varchar(255)
);
