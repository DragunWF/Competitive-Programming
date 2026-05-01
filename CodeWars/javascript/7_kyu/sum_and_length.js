// https://www.codewars.com/kata/571965ccdf7fdb10a00000ea/train/javascript

function sumLength(array) {
  let positiveSumCount = 0;
  let negativeNumCount = 0;
  let zeroCount = 0;
  for (let num of array) {
    if (num > 0) {
      positiveSumCount += num;
    } else if (num < 0) {
      negativeNumCount++;
    } else {
      zeroCount++;
      if (zeroCount % 2 === 1) {
        negativeNumCount++;
      }
    }
  }
  return `${positiveSumCount} ${negativeNumCount}`;
}
