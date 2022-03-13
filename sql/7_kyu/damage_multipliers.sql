-- https://www.codewars.com/kata/5ab828bcedbcfc65ea000099/train/sql

SELECT 
  pokemon_name,
  p.str * m.multiplier AS modifiedstrength,
  m.element
FROM pokemon p
JOIN multipliers m ON m.id = p.element_id
WHERE p.str * m.multiplier >= 40
ORDER BY modifiedStrength DESC