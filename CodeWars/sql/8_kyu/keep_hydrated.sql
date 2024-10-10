-- https://www.codewars.com/kata/582cb0224e56e068d800003c

SELECT 
  id,
  hours,
  FLOOR(0.5 * hours) AS liters
FROM cycling