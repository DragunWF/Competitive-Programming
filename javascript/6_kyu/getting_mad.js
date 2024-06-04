// https://www.codewars.com/kata/593a061b942a27ac940000a7

function gettingMad(array) {
  const values = [];
  for (let i = 0; i < array.length; i++) {
    for (let j = 0; j < array.length; j++) {
      if (i !== j) {
        values.push(Math.abs(array[i] - array[j]));
      }
    }
  }
  return Math.min(...values);
}
