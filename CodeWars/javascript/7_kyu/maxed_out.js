// https://www.codewars.com/kata/584bf3b969ebc573ed00000f/train/javascript

function maxedOut(arr) {
  let total = 0;
  for (let num of arr) {
    total += num ** 3;
  }
  if (total <= Number.MAX_SAFE_INTEGER) {
    return total;
  }
  return "You've pushed me to the max!";
}

function test() {
  console.log(maxedOut([34433, 7676, 5432, 9645, 3245, 6664, 4223, 1122357]));
}

test();
