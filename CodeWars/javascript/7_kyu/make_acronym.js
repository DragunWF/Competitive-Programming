// https://www.codewars.com/kata/57a60bad72292d3e93000a5a/train/javascript

function toAcronym(inp) {
  const words = inp.split(" ");
  const letters = [];
  for (let word of words) {
    letters.push(word[0]);
  }
  return letters.join("").toUpperCase();
}
