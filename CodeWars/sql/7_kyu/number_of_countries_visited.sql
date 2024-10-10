-- https://www.codewars.com/kata/66c71c893759d440748154f8/train/sql

SELECT people.name, COUNT(DISTINCT visits.country_id) AS countries_visited
FROM visits
RIGHT JOIN people ON people.id = visits.person_id
GROUP BY people.name
ORDER BY countries_visited DESC, people.name