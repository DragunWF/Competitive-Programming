-- https://www.codewars.com/kata/58113a64e10b53ec36000293/train/sql

SELECT *
FROM departments d
WHERE EXISTS (
  SELECT department_id
  FROM sales s
  WHERE d.id = s.department_id AND price > 98
)