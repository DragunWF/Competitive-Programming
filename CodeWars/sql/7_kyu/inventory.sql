-- https://www.codewars.com/kata/5a8eb3fb57c562110f0000a1/train/sql

SELECT id, name, stock
FROM products
WHERE stock <= 2 AND producent = "CompanyA"
ORDER BY id