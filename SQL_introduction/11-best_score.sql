-- List records with score >= 10, showing score then name, ordered by score desc
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
