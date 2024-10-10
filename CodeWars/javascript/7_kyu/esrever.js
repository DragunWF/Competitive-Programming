// https://www.codewars.com/kata/5413759479ba273f8100003d/train/javascript

reverse = function (array) {
  const reversed = [];
  for (let i = array.length - 1; i >= 0; i--) {
    reversed.push(array[i]);
  }
  return reversed;
};
