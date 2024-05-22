-- List the number of records with same score in the table
-- Records are ordered by descending count
SELECT `score`, COUNT(*) AS `number`
FROM `second__table`
GROUP BY `score`
ORDER BY `number` DESC;
