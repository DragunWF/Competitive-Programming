// https://www.codewars.com/kata/570f6436b29c708a32000826

function firstNonRepeated(str) {
  const set = [...new Set(str)];
  for (let element of set) {
    if (count(element, str) === 1) {
      return element;
    }
  }
  return null;
}

function count(char, str) {
  let count = 0;
  for (let i = 0; i < str.length; i++) {
    if (char === str[i]) {
      count++;
    }
  }
  return count;
}
