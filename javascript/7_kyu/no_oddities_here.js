// https://www.codewars.com/kata/51fd6bc82bc150b28e0000ce/train/javascript

function noOdds(values) {
  const output = [];
  for (let num of values) {
    if (num % 2 === 0) {
      output.push(num);
    }
  }
  return output;
}
