-- Creates database and table is same database
USE hbtn_0d_usa;
SELECT cities.id, cities.name FROM cities, states WHERE state.name = 'California' AND cities.id = ??? ORDER BY cities.id DESC;
