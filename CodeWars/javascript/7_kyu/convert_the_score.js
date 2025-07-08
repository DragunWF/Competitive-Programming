// https://www.codewars.com/kata/5b6c220fa0a661fbf200005d/train/javascript

function scoreboard(string) {
  const words = string.split(" ");
  const firstNumWord = words[words.length - 2];
  const secondNumWord = words[words.length - 1];
  return [convertWordToNum(firstNumWord), convertWordToNum(secondNumWord)];
}

function convertWordToNum(numWord) {
  const numWords = {
    nil: 0,
    one: 1,
    two: 2,
    three: 3,
    four: 4,
    five: 5,
    six: 6,
    seven: 7,
    eight: 8,
    nine: 9,
  };
  return numWords[numWord];
}
