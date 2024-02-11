// https://www.codewars.com/kata/570523c146edc287a50014b1

function numberJoy(n) {
  const digitSum = n
    .toString()
    .split("")
    .reduce((a, b) => Number(a) + Number(b));
  const reversed = digitSum.toString().split("");
  reversed.reverse();
  return Number(reversed.join("")) * digitSum === n;
}

// Test code
const value = 1729;
console.log(
  value
    .toString()
    .split("")
    .reduce((a, b) => Number(a) + Number(b))
);
