// https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

function count(chr, str) {
  let count = 0;
  for (let c of str) if (chr === c) count++;
  return count > 1;
}

function duplicateEncode(word) {
  let output = "";
  word = word.toLowerCase();
  for (let chr of word) output += count(chr, word) ? ")" : "(";
  return output;
}
