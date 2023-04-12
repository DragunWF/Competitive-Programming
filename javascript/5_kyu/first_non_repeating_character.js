// https://www.codewars.com/kata/52bc74d4ac05d0945d00054e

function firstNonRepeatingLetter(str) {
  const set = [...new Set(str)];
  for (let element of set) {
    if (count(element, str) === 1) {
      return element;
    }
  }
  return "";
}

function count(char, str) {
  let count = 0;
  for (let i = 0; i < str.length; i++) {
    if (char.toLowerCase() === str[i].toLowerCase()) {
      count++;
    }
  }
  return count;
}

// Not part of the solution
console.log(firstNonRepeatingLetter("stress"));
