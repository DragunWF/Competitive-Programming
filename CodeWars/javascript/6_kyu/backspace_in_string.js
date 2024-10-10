// https://www.codewars.com/kata/5727bb0fe81185ae62000ae3/train/javascript

function cleanString(s) {
  const output = [];
  for (let char of s) {
    if (char === "#") {
      output.pop();
      continue;
    }
    output.push(char);
  }
  return output.join("");
}
