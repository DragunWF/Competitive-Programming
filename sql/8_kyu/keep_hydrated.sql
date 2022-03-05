SELECT 
  id,
  hours,
  FLOOR(0.5 * hours) AS liters
FROM cycling