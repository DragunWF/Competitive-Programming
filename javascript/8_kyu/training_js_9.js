// https://www.codewars.com/kata/57216d4bcdd71175d6000560

function padIt(str, n) {
  if (n === 1) return `*${str}`;
  const half = Math.floor(n / 2);
  let output = "";
  let i = 0;
  while (i < n - half) {
    output += "*";
    i++;
  }
  output += str;
  i = 0;
  while (i < half) {
    output += "*";
    i++;
  }
  return output;
}
