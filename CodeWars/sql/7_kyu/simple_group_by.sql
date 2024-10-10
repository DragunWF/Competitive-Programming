-- https://www.codewars.com/kata/58111f4ee10b5301a7000175/train/sql

SELECT 
  age,
  COUNT(age) AS people_count
FROM people
GROUP BY age