// https://www.codewars.com/kata/52549d3e19453df56f0000fe/train/javascript

function fib(n) {
  let previousNum = 0,
    currentNum = 1;
  for (let i = 1; i < n - 1; i++) {
    let tempNum = currentNum;
    currentNum = previousNum + currentNum;
    previousNum = tempNum;
  }
  return n === 1 ? 0 : currentNum;
}

const testCases = [1, 2, 3, 4, 5];
for (let testCase of testCases) {
  console.log(fib(testCase));
}
