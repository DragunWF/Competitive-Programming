// https://www.codewars.com/kata/557cffec8c3e8e55cc00010f/train/javascript

function countZeros(n) {
  let zeroCount = 0;
  for (let i = 1; i <= n; i++) {
    zeroCount += getZeroCountOnNum(i);
  }
  return zeroCount;
}

function getZeroCountOnNum(n) {
  const strNum = String(n);
  let count = 0;
  for (let digit of strNum) {
    if (digit === "0") {
      count++;
    }
  }
  return count;
}
