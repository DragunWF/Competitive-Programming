-- https://www.codewars.com/kata/593ef0e98b90525e090000b9/train/sql

SELECT 
  th.id, th.heads, th.arms,
  bm.legs, bm.tails,
  CASE
    WHEN th.heads > th.arms OR 
         bm.tails > bm.legs THEN 'BEAST'
    ELSE 'WEIRDO'
  END AS species
FROM top_half th
JOIN bottom_half bm USING (id)
ORDER BY species