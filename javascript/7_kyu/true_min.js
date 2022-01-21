// https://www.codewars.com/kata/52378b3ee72f21e1ea000045

function min(a, b) {
  a = a === null ? 0 : a;
  b = b === null ? 0 : b;
  if (isNaN(a) || isNaN(b)) return NaN;
  return a < b ? a : b;
}
