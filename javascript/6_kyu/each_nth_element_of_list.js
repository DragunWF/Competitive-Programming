// https://www.codewars.com/kata/5a077e8106d5b654b800004f/train/javascript

function each(n, xs) {
  const output = [];
  if (n > 0) {
    for (let i = 0; i < xs.length; i++) {
      if ((i + 1) % n === 0) {
        output.push(xs[i]);
      }
    }
  } else if (n < 0) {
    for (let i = xs.length - 1, j = 1; i >= 0; i--, j++) {
      if (j % Math.abs(n) === 0) {
        output.push(xs[i]);
      }
    }
  }
  return output;
}
