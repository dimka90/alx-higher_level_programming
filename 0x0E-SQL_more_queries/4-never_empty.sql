-- Added  a script that creates the table id_not_null on your MySQL server
-- a script that edit the content the id attrbite by setting it not null with a default value of 1
CREATE TABLE IF NOT EXISTS id_not_null(
id INT DEFAULT 1,
name VARCHAR(256)
);
