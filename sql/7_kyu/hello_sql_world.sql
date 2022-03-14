-- https://www.codewars.com/kata/581283eb0a5fb13e06000020/train/sql

-- With creating the table
CREATE TABLE kata(Greeting VARCHAR(12));

INSERT INTO kata
VALUES ('hello world!');

SELECT greeting AS "Greeting"
FROM kata

-- Without creating the table
SELECT 'hello world!' AS "Greeting"
