// https://leetcode.com/problems/chunk-array/

/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function (arr, size) {
  const output = [];
  let row = [];
  for (let i = 0, n = 1; i < arr.length; i++, n++) {
    row.push(arr[i]);
    if (n % size === 0) {
      output.push([...row]);
      row = [];
    }
  }
  if (row.length) {
    output.push(row);
  }
  return output;
};
