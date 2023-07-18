// https://www.codewars.com/kata/5ce399e0047a45001c853c2b

function partsSums(ls) {
  const output = [];
  let sum = 0;
  for (let i = ls.length - 1; i >= 0; i--) {
    sum += ls[i];
    output.unshift(sum);
  }
  output.push(0);
  return output;
}

const ls = [0, 1, 3, 6, 10];
console.log(partsSums(ls));
