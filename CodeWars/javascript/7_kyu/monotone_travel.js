// https://www.codewars.com/kata/54466996990c921f90000d61/train/javascript

var isMonotone = function (arr) {
  for (let i = 1; i < arr.length; i++) {
    const prev = arr[i - 1];
    const current = arr[i];
    if (current < prev) {
      return false;
    }
  }
  return true;
};

function test() {
  console.log(isMonotone([1, 2, 3]) == true);
  console.log(isMonotone([1, 1, 2]) == true);
  console.log(isMonotone([1]) == true);
  console.log(isMonotone([3, 2, 1]) == false);
  console.log(isMonotone([3, 2, 2]) == false);
}

test();
