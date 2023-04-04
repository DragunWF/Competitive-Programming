// https://www.codewars.com/kata/522551eee9abb932420004a0/train/javascript

function nthFibo(n) {
  if (n === 1) return 0;
  let previousNum = 0, currentNum = 1;
  for (let i = 0; i < n - 2; i++) {
    const temp = currentNum;
    currentNum = previousNum + currentNum;
    previousNum = temp;
  }
  return currentNum;
}
