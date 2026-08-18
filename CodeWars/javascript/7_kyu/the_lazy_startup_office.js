// https://www.codewars.com/kata/578fdcfc75ffd1112c0001a1/train/javascript

function binRota(arr) {
  const output = [];
  let row = 0;
  let column = 0;
  let isRight = true;

  while (row < arr.length) {
    output.push(arr[row][column]);

    if (column + 1 === arr[row].length && isRight) {
      isRight = false;
      row++;
    } else if (column - 1 < 0 && !isRight) {
      isRight = true;
      row++;
    } else if (isRight) {
      column++;
    } else {
      column--;
    }
  }

  return output;
}
