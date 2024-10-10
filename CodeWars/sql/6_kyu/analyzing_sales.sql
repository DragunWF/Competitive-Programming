-- https://www.codewars.com/kata/5dac87a0abe9f1001f39e36d/train/sql

SELECT p.name AS product_name,
       EXTRACT(YEAR FROM s.date) AS year,
       EXTRACT(MONTH FROM s.date) AS month,
       EXTRACT(DAY FROM s.date) AS day,
       SUM(sd.count * p.price) AS total
FROM sales_details sd
JOIN products p ON p.id = sd.product_id
JOIN sales s ON s.id = sd.sale_id
GROUP BY product_name, year, month, day
UNION
SELECT p.name AS product_name,
       EXTRACT(YEAR FROM s.date) AS year,
       EXTRACT(MONTH FROM s.date) AS month,
       CAST(NULL AS SMALLINT) AS day,
       SUM(sd.count * p.price) AS total
FROM sales_details sd
JOIN products p ON p.id = sd.product_id
JOIN sales s ON s.id = sd.sale_id
GROUP BY product_name, year, month
UNION
SELECT p.name AS product_name,
       EXTRACT(YEAR FROM s.date) AS year,
       CAST(NULL AS SMALLINT) AS month,
       CAST(NULL AS SMALLINT) AS day,
       SUM(sd.count * p.price) AS total
FROM sales_details sd
JOIN products p ON p.id = sd.product_id
JOIN sales s ON s.id = sd.sale_id
GROUP BY product_name, year
UNION
SELECT p.name AS product_name,
       CAST(NULL AS SMALLINT) AS year,
       CAST(NULL AS SMALLINT) AS month,
       CAST(NULL AS SMALLINT) AS day,
       SUM(sd.count * p.price) AS total
FROM sales_details sd
JOIN products p ON p.id = sd.product_id
JOIN sales s ON s.id = sd.sale_id
GROUP BY product_name
ORDER BY product_name, year, month, day