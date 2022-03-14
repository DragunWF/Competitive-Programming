-- https://www.codewars.com/kata/595a3ba3843b0cbf8e000004/train/sql

SELECT
  CASE
    WHEN SUM(number1) % 2 = 0 THEN MAX(number1)
    ELSE MIN(number1)
  END AS number1,
  CASE
    WHEN SUM(number2) % 2 = 0 THEN MAX(number2)
    ELSE MIN(number2)
  END AS number2
FROM numbers