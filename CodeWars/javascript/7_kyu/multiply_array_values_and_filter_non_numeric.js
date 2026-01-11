// https://www.codewars.com/kata/55ed875819ae85ca8b00005c/train/javascript

function multiplyAndFilter(array, multiplier) {
  const output = [];
  for (let item of array) {
    if (typeof item === "number") {
      output.push(item * multiplier);
    }
  }
  return output;
}
