// https://www.codewars.com/kata/5a3f4eace1ce0eeda600003d/train/javascript

function swapTwo(array, a, b) {
  const firstAIndex = array.indexOf(a);
  const lastBIndex = getLastIndexOf(array, b);
  const temp = array[firstAIndex];
  array[firstAIndex] = array[lastBIndex];
  array[lastBIndex] = temp;
  return array;
}

function getLastIndexOf(array, value) {
  for (let i = array.length - 1; i >= 0; i--) {
    if (array[i] === value) {
      return i;
    }
  }
}

function test() {
  console.log(swapTwo([1, 2, 3, 4], 2, 4));
  console.log(swapTwo([9, 3, 1, 2, 3, 4, 1, 3, 3, 4, 8, 3, 7, 1, 7], 1, 3));
}

test();
