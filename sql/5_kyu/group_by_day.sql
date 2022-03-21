-- https://www.codewars.com/kata/5811597e9d278beb04000038

SELECT 
  CAST(TO_CHAR(created_at, 'YYYY-MM-DD') AS DATE) AS day,
  description,
  COUNT(created_at) AS count
FROM events
WHERE name = 'trained'
GROUP BY day, description
ORDER BY day