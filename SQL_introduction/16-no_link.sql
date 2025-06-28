-- List all records with a non-null and non-empty name, show score and name, order by score descending
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
