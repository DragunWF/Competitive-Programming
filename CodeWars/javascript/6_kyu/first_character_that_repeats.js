// https://www.codewars.com/kata/54f9f4d7c41722304e000bbb/train/javascript

function firstDup(str) {
  const set = [...new Set(str)];
  for (let element of set) {
    if (count(element, str) > 1) {
      return element;
    }
  }
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
