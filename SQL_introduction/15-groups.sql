-- List the number of records for each score, label count as 'number', order by number descending
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
