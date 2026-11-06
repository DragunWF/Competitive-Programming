// https://www.codewars.com/kata/5732d3c9791aafb0e4001236/train/javascript

function roundIt(n) {
  const decimalSplit = String(n).split(".");
  const leftDigitCount = decimalSplit[1].length;
  const rightDigitCount = decimalSplit[0].length;
  let result;
  if (leftDigitCount > rightDigitCount) {
    result = Math.ceil(n);
  } else if (rightDigitCount > leftDigitCount) {
    result = Math.floor(n);
  } else {
    result = Math.round(n);
  }
  return result;
}
