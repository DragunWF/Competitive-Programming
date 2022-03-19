// https://www.codewars.com/kata/52aae14aa7fd03d57400058f/train/javascript

function removeZeros(array) {
  let output = [];
  let zeros = [];
  for (let item of array) {
    if (item === 0 || item === "0") zeros = [...zeros, item];
    else output = [...output, item];
  }
  for (let zero of zeros) output = [...output, zero];
  return output;
}

console.log(removeZeros([7, 2, 3, 0, 4, 6, 0, 0, 13, 0, 78, 0, 0, 19, 14]));
