CREATE DATABASE users;
\c users

CREATE TABLE user_name (id serial, first_name varchar(255), last_name varchar(255), nickname varchar(500));

INSERT INTO user_name (first_name, last_name, nickname)
VALUES
	('Sergey', 'Kremenckij', 'Kremen'),
	('Anna', 'Shevchenko', 'Sheva'),
	('Andrey', 'Kravcov', 'Krava'),
	('Stepan', 'Kotlov', 'Kotel'),
	('Vasya', 'Pupkin', 'Pupok');

SELECT * FROM user_name;


UPDATE user_name
SET last_name = 'Kremenckiy'
WHERE last_name = 'Kremenckij';

SELECT * FROM user_name;

DELETE FROM user_name
WHERE id=4
RETURNING *;



ALTER TABLE user_name ADD COLUMN date_update varchar(50);

UPDATE user_name
SET date_update = CURRENT_DATE;

SELECT * FROM user_name;

CREATE TABLE user_name_backup (id serial, first_name varchar(255), last_name varchar(255), nickname varchar(500));
INSERT INTO user_name_backup (first_name, last_name, nickname)
VALUES
	('Sergey', 'Kremenckij', 'Kremen'),
	('Anna', 'Shevchenko', 'Sheva'),
	('Andrey', 'Kravcov', 'Krava'),
	('Stepan', 'Kotlov', 'Kotel'),
	('Vasya', 'Pupkin', 'Pupok');






SELECT * FROM user_name CROSS JOIN user_name_backup;
SELECT * FROM user_name NATURAL INNER JOIN user_name_backup;

SELECT * FROM user_name ORDER BY first_name, last_name, nickname ASC
FETCH FIRST ROW ONLY;


ALTER TABLE user_name_backup ADD COLUMN date_update varchar(50);


SELECT * FROM user_name
NATURAL INNER JOIN user_name_backup; 



TRUNCATE user_name_backup;