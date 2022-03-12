-- https://www.codewars.com/kata/590ba881fe13cfdcc20001b4/train/sql
-- Switched to SQLite 3.2.8

SELECT *
FROM travelers
WHERE country NOT IN ("Canada", "Mexico", "USA")
