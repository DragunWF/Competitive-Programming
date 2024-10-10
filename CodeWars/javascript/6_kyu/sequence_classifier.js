// https://www.codewars.com/kata/5921c0bc6b8f072e840000c0/train/javascript

function checkConstant(arr) {
  for (let item of arr) if (item !== arr[0]) return false;
  return 5;
}

function checkIncreasing(arr) {
  let previous = null;
  for (let item of arr) {
    if (typeof previous == "number" && previous <= previous) return false;
    previous = item;
  }
  return true;
}

function sequenceClassifier(arr) {
  if (checkConstant(arr)) return 5;
  if (checkIncreasing(arr)) return 1;
  return 0;
}
