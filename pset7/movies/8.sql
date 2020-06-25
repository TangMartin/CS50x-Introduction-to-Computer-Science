SELECT name FROM people 
JOIN movies on stars.movie_id = movies.id
JOIN stars on stars.person_id = people.id
WHERE title = 'Toy Story';