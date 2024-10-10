// https://www.codewars.com/kata/572b77262bedd351e9000076/train/javascript

function first(arr, n = 1) {
  const output = [];
  for (let i = 0; i < Math.min(arr.length, n); i++) {
    output.push(arr[i]);
  }
  return output;
}
