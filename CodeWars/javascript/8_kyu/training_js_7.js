// https://www.codewars.com/kata/57202aefe8d6c514300001fd/train/javascript

function saleHotdogs(n) {
  if (n < 5) return 100 * n;
  return n >= 5 && n < 10 ? 95 * n : 90 * n;
}
