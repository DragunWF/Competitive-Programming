-- https://www.codewars.com/kata/5802e32dd8c944e562000020/train/sql

SELECT 
  p.id,
  p.name,
  p.isbn,
  p.company_id,
  p.price,
  c.name AS company_name
FROM products p
JOIN companies c ON
  p.company_id = c.id