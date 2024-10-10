// https://www.codewars.com/kata/51675d17e0c1bed195000001/train/javascript

function solution(digits) {
  const arr = digits.split("").map((n) => parseInt(n));
  arr.sort((a, b) => b - a);
  return parseInt(arr.join("").substring(0, 5));
}

// Not part of the solution, just testing
function test() {
  console.log(solution("1234567890"));
}

test();
