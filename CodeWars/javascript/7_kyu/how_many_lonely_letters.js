// https://www.codewars.com/kata/69cda5b85599f307742ce70a/train/javascript

function countLonelyLetters(text) {
  const asciiLetters = "abcdefghijklmnopqrstuvwxyz";

  text = text.toLowerCase();
  const charCodes = getCharCodes(text);

  let lonelyLetters = 0;
  const letterCounter = getCounter(text);
  for (let i = 0; i < text.length; i++) {
    if (!asciiLetters.includes(text[i])) continue;

    if (text[i] === "a" || text[i] === "z") {
      if (
        (text[i] === "a" &&
          letterCounter[text[i]] === 1 &&
          !charCodes.includes(charCodes[i] + 1)) ||
        (text[i] === "z" &&
          letterCounter[text[i]] === 1 &&
          !charCodes.includes(charCodes[i] - 1))
      ) {
        lonelyLetters++;
      }
    } else {
      if (
        letterCounter[text[i]] === 1 &&
        !charCodes.includes(charCodes[i] + 1) &&
        !charCodes.includes(charCodes[i] - 1)
      ) {
        lonelyLetters += 1;
      }
    }
  }
  return lonelyLetters;
}

function getCharCodes(text) {
  const charCodes = [];
  for (let i = 0; i < text.length; i++) {
    charCodes.push(text.charCodeAt(i));
  }
  return charCodes;
}

function getCounter(text) {
  const counter = {};
  for (let char of text) {
    if (!Object.keys(counter).includes(char)) {
      counter[char] = 1;
    } else {
      counter[char]++;
    }
  }
  return counter;
}
