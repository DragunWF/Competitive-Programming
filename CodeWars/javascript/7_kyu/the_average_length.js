// https://www.codewars.com/kata/5a430359e1ce0e35540000b1/train/javascript

function averageLength(matrix) {
  let totalLength = 0;
  for (let array of matrix) {
    totalLength += array.length;
  }

  const average = Math.round(totalLength / matrix.length);
  const output = [];
  for (let array of matrix) {
    let strWithAvgLength = "";
    for (let i = 0; i < average; i++) {
      strWithAvgLength += array[0];
    }
    output.push(strWithAvgLength);
  }

  return output;
}
