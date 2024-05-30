// https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118/train/javascript

function distinct(a) {
  const output = [];
  for (let num of a) {
    if (!output.includes(num)) {
      output.push(num);
    }
  }
  return output;
}
