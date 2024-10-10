-- https://www.codewars.com/kata/5ac698cdd325ad18a3000170/train/sql

SELECT 
  name,
  SUM(won) AS won,
  SUM(lost) AS lost
FROM fighters
WHERE move_id NOT IN (1, 2, 3)
GROUP BY name
ORDER BY won DESC
LIMIT 6
