// https://www.codewars.com/kata/55c6126177c9441a570000cc

function orderWeight(strng) {
  const arr = strng.split(" ");
  arr.sort();
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length - 1; j++) {
      if (sumDigits(arr[j]) > sumDigits(arr[j + 1])) {
        const temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
  return arr.join(" ");
}

function sumDigits(element) {
  return element.split("").reduce((a, b) => Number(a) + Number(b));
}

// Not part of the solution
function test() {
  console.log(orderWeight("103 123 4444 99 2000"));
  console.log(orderWeight("2000 10003 1234000 44444444 9999 11 11 22 123"));
}

test();
