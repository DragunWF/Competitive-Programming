// https://www.codewars.com/kata/57256064856584bc47000611

function howManySmaller(arr, n) {
  let count = 0;
  for (let num of arr) {
    if (Math.round(num * 100) / 100 < n) {
      count++;
    }
  }
  return count;
}

// Not part of the solution, just testing
function test() {
  console.log(howManySmaller([1.234, 1.235, 1.228], 1.24));
}

test();
