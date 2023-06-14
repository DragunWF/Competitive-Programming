// https://www.codewars.com/kata/59c633e7dcc4053512000073/train/javascript

function solve(s) {
  return s
    .split(/[aeiou]/)
    .map((a) => getConsonantValue(a))
    .sort((a, b) => b - a)[0];
}

function getConsonantValue(str) {
  const alphabets = "abcdefghijklmnopqrstuvwxyz";
  let value = 0;
  for (let character of str) {
    value += alphabets.indexOf(character) + 1;
  }
  return value;
}

// Not part of the solution
console.log(solve("strength"));
