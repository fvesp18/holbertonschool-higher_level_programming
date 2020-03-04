-- Creates database and table is same database
SELECT cities.id, cities.name, states.name FROM cities, states WHERE states.name IS NOT NULL AND states.id = cities.state_id ORDER BY cities.id ASC;
