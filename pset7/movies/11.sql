SELECT movies.title FROM movies
JOIN ratings on ratings.movie_id = movies.id
JOIN stars on stars.movie_id = movies.id
JOIN people on people.id = stars.person_id
WHERE people.name = 'Chadwick Boseman'
ORDER By ratings.rating DESC
LIMIT 5;