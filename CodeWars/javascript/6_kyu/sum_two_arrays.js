// https://www.codewars.com/kata/59c3e8c9f5d5e40cab000ca6/train/javascript

function addArrays(array1, array2) {
  if (!array1.length) return array2;
  if (!array2.length) return array1;
  const arrSumStr = (getArraySum(array1) + getArraySum(array2)).toString();
  const output = [];
  let isNegative = false;
  for (let digit of arrSumStr) {
    if (digit === "-") {
      isNegative = true;
      continue;
    }
    output.push(parseInt(digit));
  }
  if (isNegative) output[0] = -output[0];
  return output;
}

function getArraySum(array) {
  let strNum = "";
  for (let num of array) {
    strNum += num;
  }
  return parseInt(strNum);
}
