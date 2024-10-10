// https://www.codewars.com/kata/5274e122fc75c0943d000148/train/javascript

function groupByCommas(n) {
  let output = [];
  for (let str = String(n), i = str.length - 1, j = 1; i >= 0; i--, j++) {
    output.unshift(str.charAt(i));
    if (j % 3 === 0 && i !== 0) {
      output.unshift(",");
    }
  }
  return output.join("");
}

// Not part of the solution
function test() {
  console.log(groupByCommas(1000));
}

test();
