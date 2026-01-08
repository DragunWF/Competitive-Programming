// https://www.codewars.com/kata/57e8c68c97a05990b10000c3/train/javascript

function collatz(n, count = 1) {
  if (n <= 1) return count;
  return collatz(n % 2 === 0 ? n / 2 : n * 3 + 1, count + 1);
}

function test() {
  console.log(collatz(2)); // 2
  console.log(collatz(4)); // 3
  console.log(collatz(6)); // 9
}

test();
