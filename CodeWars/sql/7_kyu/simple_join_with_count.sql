-- https://www.codewars.com/kata/580918e24a85b05ad000010c/train/sql

SELECT
  p.id,
  p.name,
  COUNT(t.people_id) AS toy_count
FROM people p
JOIN toys t ON
  t.people_id = p.id
GROUP BY p.id