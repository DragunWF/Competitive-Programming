// https://www.codewars.com/kata/5a523566b3bfa84c2e00010b/train/javascript

function minSum(arr) {
  arr.sort((a, b) => b - a);
  const products = [];
  for (let i = 0; i < Math.floor(arr.length / 2); i++) {
    products.push(arr[i] * arr[arr.length - (i + 1)]);
  }
  return products.reduce((a, b) => a + b);
}

// Test Code
console.log(minSum([5, 4, 2, 3]));
console.log(minSum([12, 6, 10, 26, 3, 24]));
