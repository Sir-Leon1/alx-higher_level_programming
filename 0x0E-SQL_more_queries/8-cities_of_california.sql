-- Lists all cities of CA in the DB hbtn_0d_usa
-- Results are ordered by ascending cities.id
SELECT `id`,  `name` FROM `cities` WHERE `state_id` IN (SELECT `id` FROM `states` WHERE `name` = "California") ORDER BY `id`;
