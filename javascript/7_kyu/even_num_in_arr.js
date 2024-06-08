// https://www.codewars.com/kata/5a431c0de1ce0ec33a00000c/train/javascript

function evenNumbers(array, number) {
  const output = [];
  for (let i = array.length - 1; i >= 0; i--) {
    if (array[i] % 2 === 0) output.unshift(array[i]);
    if (output.length === number) break;
  }
  return output;
}
