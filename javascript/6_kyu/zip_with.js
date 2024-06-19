// https://www.codewars.com/kata/5825792ada030e9601000782/train/javascript

function zipWith(fn, a0, a1) {
  const output = [];
  for (let i = 0; i < Math.min(a0.length, a1.length); i++) {
    output.push(fn(a0[i], a1[i]));
  }
  return output;
}
