// https://www.codewars.com/kata/5612ab201830eb000f0000c0/train/javascript

function findMinNum(num) {
  let divisors = 1;
  let x = 0;
  while (true) {
    x++;
    for (let i = 1; i <= x; i++) if (x % i === 0) divisors++;
    if (divisors === num) break;
    divisors = 0;
  }
  return x;
}

console.log(findMinNum(8)); // 24
console.log(findMinNum(7)); // 64
