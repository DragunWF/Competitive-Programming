-- https://www.codewars.com/kata/5ab7a736edbcfc8e62000007/train/sql

SELECT 
  ss.senshi_name AS sailor_senshi,
  ss.real_name_jpn AS real_name,
  c.name AS cat,
  s.school
FROM sailorsenshi ss
LEFT JOIN cats c 
  ON c.id = ss.cat_id
LEFT JOIN schools s 
  ON s.id = ss.school_id