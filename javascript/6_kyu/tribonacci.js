// https://www.codewars.com/kata/556deca17c58da83c00002db/train/javascript

function tribonacci(signature, n) {
  const seq = [];
  for (let i = 0; i < n; i++) {
    if (i < signature.length) {
      seq.push(signature[i]);
      continue;
    }
    seq.push(seq[i - 1] + seq[i - 2] + seq[i - 3]);
  }
  return seq;
}

// Not part of the solution
function test() {
  const testCases = [
    [[1, 1, 1], 10],
    [[0, 0, 1], 10],
    [[1, 2, 3], 10],
    [[3, 2, 1], 10],
  ];
  for (let testCase of testCases) {
    console.log(tribonacci(testCase[0], testCase[1]));
  }
}

test();
