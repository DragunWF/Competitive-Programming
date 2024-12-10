// https://www.codewars.com/kata/58dace86b809ca6c62000ccf/train/javascript

function hasPair(arr, sum) {
  let left = 0;
  let right = arr.length - 1;
  while (left < right) {
    let currentSum = arr[left] + arr[right];
    if (currentSum > sum) {
      right--;
    } else if (currentSum < sum) {
      left++;
    } else {
      return true;
    }
  }
  return false;
}
