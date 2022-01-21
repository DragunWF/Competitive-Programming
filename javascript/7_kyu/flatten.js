// https://www.codewars.com/kata/5250a89b1625e5decd000413

var flatten = function (array) {
  const output = [];
  for (i = 0; i < array.length; i++) {
    if (typeof array[i] === "object") output.push(...array[i]);
    else return array;
  }
  return output;
};
