// https://www.codewars.com/kata/523f5d21c841566fde000009

function arrayDiff(a, b) {
  let x = [];
  for (i of a) {
    if (!b.includes(i)) x.push(i);
  }
  return x;
}
