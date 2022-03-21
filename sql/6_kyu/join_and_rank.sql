-- https://www.codewars.com/kata/58094559c47d323ebd000035/

SELECT 
  RANK() OVER(ORDER BY COUNT(s.sale) DESC) AS sale_rank, 
  p.id,
  p.name,
  COUNT(s.sale) AS sale_count
FROM people p
JOIN sales s ON s.people_id = p.id
GROUP BY p.id
ORDER BY sale_count DESC