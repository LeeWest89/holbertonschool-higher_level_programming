--  lists all cities contained in the database in ascending order based on cities.id
SELECT cities.id, cities.name, states.name FROM cities, states
WHERE cities.state_id = states.id ORDER BY cities.id ASC;
