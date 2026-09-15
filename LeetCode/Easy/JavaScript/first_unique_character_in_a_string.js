// https://leetcode.com/problems/first-unique-character-in-a-string/

/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function (s) {
  const counter = createCounter(s);
  for (let i = 0; i < s.length; i++) {
    const char = s.charAt(i);
    if (counter[char] === 1) {
      return i;
    }
  }
  return -1;
};

let createCounter = function (s) {
  const counter = {};
  for (let char of s) {
    if (char in counter) {
      counter[char]++;
    } else {
      counter[char] = 1;
    }
  }
  return counter;
};
