-- List cities in California without using JOIN, sorted by cities.id ascending
SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY id ASC;
