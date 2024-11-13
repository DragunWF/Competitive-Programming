// https://leetcode.com/problems/sort-the-people/description/

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const output = [];
    for (let i = 0; i < arr.length; i++) {
        if (fn(arr[i], i)) {
            output.push(arr[i])
        }
    }
    return output;
};