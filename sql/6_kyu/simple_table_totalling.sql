-- https://www.codewars.com/kata/5809575e166583acfa000083

SELECT
  RANK() OVER(ORDER BY SUM(points) DESC),
  CASE
    WHEN clan = '' THEN '[no clan specified]'
    ELSE clan
  END AS clan,
  SUM(points) AS total_points,
  COUNT(name) AS total_people
FROM people
GROUP BY clan
ORDER BY total_points DESC