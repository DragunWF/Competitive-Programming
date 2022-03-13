-- https://www.codewars.com/kata/5e5f09dc0a17be0023920f6f/train/sql

SELECT capital
FROM countries
WHERE 
  country LIKE "E%" AND
  continent IN ("Africa", "Afrika")
ORDER BY capital
LIMIT 3