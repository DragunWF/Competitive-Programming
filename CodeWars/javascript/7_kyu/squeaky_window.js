// https://www.codewars.com/kata/55f8b5b09ec923860200000f/train/javascript

function sliding(nums, k) {
  const output = [];
  for (let i = 0, j = k; j <= nums.length; i++, j++) {
    let max = nums[i];
    for (let x = i + 1; x < j; x++) {
      if (nums[x] > max) {
        max = nums[x];
      }
    }
    output.push(max);
  }
  return output;
}

// test code
console.log(sliding([1, 3, -1, -3, 5, 3, 6, 7], 3));
console.log(sliding([1, 2, 3, 4], 1));
console.log(sliding([7, 2, 4], 2));
