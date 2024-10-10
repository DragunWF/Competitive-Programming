// https://www.codewars.com/kata/5208f99aee097e6552000148/train/javascript

function solution(string) {
  let output = "";
  for (let chr of string) 
    output += chr.toUpperCase() == chr ? ` ${chr}` : chr;
  return output;
}
