// https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/javascript

String.prototype.toJadenCase = function () {
  let output = [];
  for (let word of this.split(" "))
    output.push(`${word[0].toUpperCase()}${word.substring(1)}`);
  return output.join(" ");
};
