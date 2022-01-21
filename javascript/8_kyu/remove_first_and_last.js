// https://www.codewars.com/kata/570597e258b58f6edc00230d

function array(arr) {
  let word = arr.split(",");
  word.shift(), word.pop();
  if (word.length < 1) return null;
  return word.join(" ");
}
