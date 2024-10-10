// https://www.codewars.com/kata/515e271a311df0350d00000f/train/javascript

function squareSum(numbers) {
  return numbers.reduce((a, b) => a + b * b, 0);
}

// Not part of the solution
function test() {
  console.log(squareSum([1, 2, 2]));
}

test();
