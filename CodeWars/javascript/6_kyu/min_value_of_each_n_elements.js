// https://www.codewars.com/kata/5831c5f8ac6a11e3380002de/train/javascript

function minValue(arr, n) {
  if (n === 1) return arr;
  const output = [];
  for (let i = 0; i <= arr.length - n; i++) {
    let min = arr[i];
    for (let j = i + 1; j < i + n && i < arr.length; j++) {
      if (arr[j] < min) {
        min = arr[j];
      }
    }
    output.push(min);
  }
  return output;
}
