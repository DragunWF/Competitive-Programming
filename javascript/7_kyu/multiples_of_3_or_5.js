// https://www.codewars.com/kata/514b92a657cdc65150000006

function solution(number) {
  let array = [];
  for (let i = 0; i < number; i++) {
    if (i % 3 === 0 || i % 5 === 0) array.push(i);
  }
  if (array.length < 1) return 0;
  return array.reduce((a, b) => a + b);
}
