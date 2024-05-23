-- List all shows contained in the DB hbtn_0d_tvshows
-- Displays NULL for shows without genres.
-- Records are ordered by ascending tv_shows
SELECT s.`tilte`, g.`genre_id` FROM `tv_shows` AS s LEFT JOIN `tv_show_genres` AS g ON s.`id` = g.`show_id` ORDER BY s.`title`, g.`genre_id`;
