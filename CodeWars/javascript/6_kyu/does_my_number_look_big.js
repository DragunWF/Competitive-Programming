// https://www.codewars.com/kata/5287e858c6b5a9678200083c/train/javascript

function narcissistic(value) {
  const strValue = value.toString();
  let total = 0;
  for (let num of strValue) {
    total += Math.pow(Number(num), strValue.length);
  }
  return total === value;
}
