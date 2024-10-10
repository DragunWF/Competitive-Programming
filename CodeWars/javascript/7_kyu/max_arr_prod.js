// https://www.codewars.com/kata/5a63948acadebff56f000018/train/javascript

function maxProduct(numbers, size) {
  numbers.sort((a, b) => b - a);
  let maxProduct = numbers[0];
  for (let i = 1; i < size; i++) {
    maxProduct *= numbers[i];
  }
  return maxProduct;
}

// Test code
console.log(maxProduct([4, 3, 5], 2));
