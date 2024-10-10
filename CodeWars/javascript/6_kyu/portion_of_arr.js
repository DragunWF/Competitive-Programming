// https://www.codewars.com/kata/598e3859f289bb47ba00000a/train/javascript

function portion(a, i, n) {
  if (Math.abs(i) >= a.length || n > a.length - Math.abs(i)) {
    return -1;
  }
  const output = [];
  const isPositive = i >= 0;
  for (
    let x = isPositive ? i : a.length - 1 + i;
    output.length < n;
    isPositive ? x++ : x--
  ) {
    output.push(a[x]);
  }
  if (!isPositive) {
    output.reverse();
  }
  return output;
}

// Not part of the solution
function test() {
  const results = [portion([1, 2, 3, 4], -1, 2), portion([1, 2, 3, 4], 1, 2)];
  for (let i = 0; i < results.length; i++) {
    console.log(`Test Case #${i + 1}: ${results[i]}`);
  }
}

test();

// function portion(a, i, n) {
//   if (Math.abs(i) >= a.length || n > a.length - Math.abs(i)) {
//     return -1;
//   }
//   const output = [];
//   for (let x = i >= 0 ? i : a.length + i - 1; output.length < n; x++) {
//     output.push(a[x]);
//     console.log(output, x);
//   }
//   return output;
// }
