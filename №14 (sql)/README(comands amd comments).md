CREATE DATABASE lesson 14;
\c lesson 14;
\d
CREATE TABLE type (id SERIAL PRIMARY KEY, title VARCHAR(500));

CREATE TABLE color (id SERIAL PRIMARY KEY, title VARCHAR(500));

CREATE TABLE brand (id SERIAL PRIMARY KEY, title VARCHAR(500));

CREATE TABLE model (id SERIAL PRIMARY KEY, title VARCHAR(500), description VARCHAR(500), id_brand INT NOT NULL DEFAULT 0, id_type INT NOT NULL DEFAULT 0, id_color INT NOT NULL DEFAULT 0);


INSERT INTO brand(title) VALUES
('ZAZ'),
('PORSHE'),
('MERCEDES'),
('JEEP');

INSERT INTO type(title) VALUES
('Хетчбек'),
('Универсал'),
('Купе'),
('Кроссовер');

INSERT INTO color(title) VALUES
('Золотой'),
('Ржавый'),
('Серый'),
('Красненький');


SELECT * FROM brand;
SELECT * FROM type;
SELECT * FROM color;


INSERT INTO model (title, description, id_brand, id_type, id_color) VALUES
('Запоржец 969', 'Машина Деда', '1', '1', '2'),
('Porshe 911', 'Машина детства', '2', '1', '1'),
('Mercedes Long', 'Для крутых парней', '3', '3', '3'),
('Nissan Juke', 'Для наркученных девушек', '4', '4', '4');


SELECT * FROM brand;
SELECT * FROM type;
SELECT * FROM color;
SELECT * FROM model;


# связываю все 4 таблицы, получаю данные, которые соответствуют друг другу во всех таблицах
SELECT model.title, model.description, brand.title, type.title, color.title
FROM model
INNER JOIN brand ON model.id_brand = brand.id
INNER JOIN type ON model.id_type = type.id
INNER JOIN color ON model.id_color = color.id;


# сортирую данные по алфивиту (desc) и вывожу только 3 из них и начинаю от 1-го (то есть 3 последних)
SELECT model.title, model.description, brand.title, type.title, color.title
FROM model
INNER JOIN brand ON model.id_brand = brand.id
INNER JOIN type ON model.id_type = type.id
INNER JOIN color ON model.id_color = color.id
ORDER BY
model.title DESC;
LIMIT 3 OFFSET 1;



# получаем только модель и бренд из левой таблицы.
SELECT model.title, brand.title
FROM model
LEFT JOIN brand ON model.id_brand = brand.id;



# получаем все поля с двух таблиц
SELECT * FROM model
FULL JOIN brand ON model.id_brand = brand.id;






