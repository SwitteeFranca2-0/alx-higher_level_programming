-- genre by id

SELECT tv_shows.title, tv_shows_genre.genre_id FROM tv_shows INNER tv_shows_genre ON tv_shows.id = tv_shows_genre.show_id ORDER BY tv_shows.title ASC, tv_shows_genre.genre_id ASC;
