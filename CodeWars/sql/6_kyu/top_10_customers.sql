-- https://www.codewars.com/kata/580d08b5c049aef8f900007c/train/sql

SELECT 
  c.customer_id,
  c.email,
  COUNT(p.payment_id) AS payments_count,
  CAST(SUM(p.amount) AS FLOAT) AS total_amount
FROM customer c
JOIN payment p USING (customer_id)
GROUP BY customer_id
ORDER BY total_amount DESC
LIMIT 10