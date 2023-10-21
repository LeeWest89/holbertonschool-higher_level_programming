-- Creates database and table, list all cities in California on database
SELECT id, name FROM cities WHERE state_id = 
(SELECT id FROM states WHERE name = 'California') ORDER BY cities.id ASC;
