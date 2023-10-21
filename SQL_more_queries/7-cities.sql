-- Creates database(hbtn_0d_usa) and table(states and cities) with ids that auto increment.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
	PRIMARY KEY (id),
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL
);
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
	PRIMARY KEY (id),
	FOREIGN KEY (state_id) REFERENCES states(id),
	id INT NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL
);
