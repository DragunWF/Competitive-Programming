// https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getSneakyNumbers = function (nums) {
  const sneakyNumbers = [];
  const seen = [];
  for (let num of nums) {
    if (!seen.includes(num)) {
      seen.push(num);
    } else if (!sneakyNumbers.includes(num)) {
      sneakyNumbers.push(num);
    }
  }
  return sneakyNumbers;
};
