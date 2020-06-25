SELECT people.name FROM directors
JOIN people on people.id = directors.person_id
JOIN ratings on ratings.movie_id = movies.id
JOin movies on movies.id = directors.movie_id
WHERE ratings.rating >= 9;