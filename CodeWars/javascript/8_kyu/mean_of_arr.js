// https://www.codewars.com/kata/563e320cee5dddcf77000158/train/javascript

function getAverage(marks) {
  return Math.floor(marks.reduce((a, b) => a + b) / marks.length);
}

// Not part of the solution
function test() {
  const cases = [
    [2, 2, 2, 2],
    [1, 2, 3, 4, 5],
  ];
  for (let i = 0; i < cases.length; i++) {
    const result = getAverage(cases[i]);
    console.log(`Test Case #${i + 1}: ${result}`);
  }
}

test();
