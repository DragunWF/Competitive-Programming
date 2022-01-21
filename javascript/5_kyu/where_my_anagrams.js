// https://www.codewars.com/kata/523a86aa4230ebb5420001e1

function anagrams(word, words) {
  word = word.split("").sort().join("");
  return words.filter((w) => {
    if (checkLetters(w, word)) return w;
  });
}

function checkLetters(element, word) {
  element = element.split("").sort().join("");
  word = word.split("").sort().join("");
  if (element === word) return true;
  return false;
}
