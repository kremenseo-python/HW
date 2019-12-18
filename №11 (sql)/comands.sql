CREATE DATABASE allfilms;
\c allfilms 

CREATE TABLE category (category_id serial, name varchar(255), last_update int);

INSERT INTO category (name, last_update)
VALUES
	('Hitman', 2001),
	('Titanic', 1998),
	('Prestige', 2005);
	





CREATE TABLE film_category (film_id serial, category_id integer);

CREATE TABLE film (film_id serial, title text, description text, release_year text, language_id integer);

CREATE TABLE language (language_id integer);

