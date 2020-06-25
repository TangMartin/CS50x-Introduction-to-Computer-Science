SELECT ratings.rating, movies.title FROM ratings
JOIN movies on movies.id = ratings.movie_id
WHERE year = 2010
ORDER by ratings.rating DESC, movies.title;