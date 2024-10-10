// https://www.codewars.com/kata/64294e2be00c71422d1f59c2/train/javascript

function f(n) {
  return n % 2 !== 0 ? n * 2 : n + n / 2;
}

// Not part of the solution
function test() {
  for (let i = 1; i <= 10; i++) {
    console.log(f(f(i)));
  }
}

test();

// function f(n) {
//     const limit = 10000000;
//     if (n > limit) {
//       return (n - limit) * 3;
//     }
//     return limit + n;
//   }
