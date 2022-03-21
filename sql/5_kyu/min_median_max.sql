-- https://www.codewars.com/kata/58167fa1f544130dcf000317/train/sql

SELECT 
  MIN(score),
  CEIL(CAST(AVG(score) AS FLOAT)) + 1 AS median,
  MAX(score)
FROM result