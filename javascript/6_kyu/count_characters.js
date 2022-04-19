// https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/javascript

function count(string) {
  const output = {};
  for (let c of string) output[c] = output[c] ? output[c] + 1 : 1;
  return output;
}

console.log(count("aba"));
