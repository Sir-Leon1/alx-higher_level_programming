-- Displays the max temp of each state
-- Order by state anme
SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;
