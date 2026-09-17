// https://www.codewars.com/kata/5681cf0be812b41721000034/train/javascript

function removeNoise(str) {
  const notAllowed = "%$&/#·@|º\\ª";
  let output = "";
  for (let char of str) {
    if (notAllowed.includes(char)) {
      continue;
    }
    output += char;
  }
  return output;
}
