// https://www.codewars.com/kata/5894318275f2c75695000146/train/javascript

function deleteDigit(n) {
  let max = 0;
  for (let i = 0, j = n.toString(); i < j.length; i++) {
    const num = Number(j.substring(0, i) + j.substring(i + 1));
    if (num > max) {
      max = num;
    }
  }
  return max;
}

// Test code
console.log(deleteDigit(152));
console.log(deleteDigit(1001));
