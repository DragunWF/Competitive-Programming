// https://www.codewars.com/kata/5566b0dd450172dfc4000005/train/javascript

let lengthOfSequence = (arr, n) => {
  if (!isCountTwo(arr, n)) return 0;
  let length = 0;
  let isSequence = false;
  for (let num of arr) {
    if (isSequence) length++;
    if (num === n) {
      if (isSequence) break;
      isSequence = true;
      length++;
    }
  }
  return length;
};

let isCountTwo = (arr, n) => {
  let count = 0;
  for (let num of arr) {
    if (n === num) count++;
    if (count > 2) return false;
  }
  return count === 2;
};
