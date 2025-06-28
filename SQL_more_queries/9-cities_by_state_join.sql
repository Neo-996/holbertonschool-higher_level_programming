-- List all cities with their corresponding state name,
-- sorted by cities.id ascending, using a single SELECT and JOIN
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
