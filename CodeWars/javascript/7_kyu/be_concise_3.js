// https://www.codewars.com/kata/56f8fe6a2e6c0dc83b0008a7/train/javascript

function sumSquares(array) {
  return array.reduce((acc, cur) => acc + cur ** 2, 0);
}
