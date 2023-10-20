-- lists all records of the table second_table as long as name is not NULL
SELECT score, name FROM second_table WHERE name IS NOT NULL
ORDER BY score DESC;
