// https://www.codewars.com/kata/529adbf7533b761c560004e5/train/javascript

function fibonacci(n, memo = {}) {
  if (memo[n] !== undefined) return memo[n];
  if (n === 0) return 0;
  if (n <= 2) return 1;
  let res = fibonacci(n - 1, memo) + fibonacci(n - 2, memo);
  memo[n] = res;
  return res;
}
