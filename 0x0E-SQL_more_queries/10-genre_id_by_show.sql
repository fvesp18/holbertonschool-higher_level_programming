-- Lists all shwos contained in htbn_0d_tvshows that have atleast one linked genre
-- ANother line of comments
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres
WHERE tv_shows.id IS NOT NULL AND tv_shows.id = tv_show_genres.show_id
GROUP BY tv_shows.title, tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
