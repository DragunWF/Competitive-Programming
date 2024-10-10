// https://www.codewars.com/kata/556021360863a1708900007b

function checkValidTrNumber(n) {
  if (typeof n !== "number") return false;
  n = n.toString();
  if (n.length !== 11) return false;
  const a = getSum(n, [0, 2, 4, 6, 8]) * 7;
  const b = getSum(n, [1, 3, 5, 7]);
  const c = getSum(n, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);
  return (a - b) % 10 === Number(n[9]) && c % 10 === Number(n[10]);
}

function getSum(n, indicies) {
  let sum = 0;
  for (let i = 0; i < n.length; i++) {
    if (indicies.includes(i)) sum += Number(n[i]);
    if (i > indicies[indicies.length - 1]) break;
  }
  return sum;
}

// Not part of the solution
function test() {
  const testCases = [6923522112, 692352217312, "x5810a78432"];
  for (let i = 0; i < testCases.length; i++) {
    console.log(checkValidTrNumber(testCases[i]));
  }
}

test();
