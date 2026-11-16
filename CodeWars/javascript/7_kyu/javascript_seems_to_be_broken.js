// https://www.codewars.com/kata/565d6d1696e154b51b000076/train/javascript

// kata modified the join method to not work
// so i made my own

function semicolonSeparationToCommaSeparation(input) {
  return customJoin(input.split(";"));
}

function customJoin(arr) {
  let output = "";
  for (let i = 0; i < arr.length; i++) {
    output += arr[i];
    if (i + 1 !== arr.length) {
      output += ",";
    }
  }
  return output;
}

function test() {
  console.log(semicolonSeparationToCommaSeparation("1;2;3"));
}

test();
