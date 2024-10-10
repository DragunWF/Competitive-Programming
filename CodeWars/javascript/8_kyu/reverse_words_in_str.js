// https://www.codewars.com/kata/57a55c8b72292d057b000594/train/javascript

function reverse(string) {
  const words = string.split(" ");
  words.reverse();
  return words.join(" ");
}
