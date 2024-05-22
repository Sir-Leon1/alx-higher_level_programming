-- Display the average temp (in fahrenheit)
-- By city ordered by descendinf temp
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
