// https://www.codewars.com/kata/5547cc7dcad755e480000004

function removeNb(n) {
  let sum = (n / 2) * (2 + n - 1);
  const sequences = [];
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= n; j++) {
      if (i * j === sum - i - j) {
        sequences.push([i, j]);
      }
    }
  }
  return sequences;
}

// Not part of the solution
function test() {
  const testCases = [26, 100];
  for (let i = 0; i < testCases.length; i++) {
    const result = removeNb(testCases[i]);
    console.log(`Test Case #${i + 1}: [${result}]`);
  }
}

test();
