// https://leetcode.com/problems/sort-by/

/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function (arr, fn) {
  const output = [...arr];
  output.sort((a, b) => fn(a) - fn(b));
  return output;
};
