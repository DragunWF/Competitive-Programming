-- https://www.codewars.com/kata/541629460b198da04e000bb9/train/java

SELECT failure_reason, SUM(1) AS cnt 
FROM interview_failures
GROUP BY failure_reason
ORDER BY cnt DESC, failure_reason 