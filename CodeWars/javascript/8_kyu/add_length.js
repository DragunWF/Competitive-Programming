// https://www.codewars.com/kata/559d2284b5bb6799e9000047/train/javascript

function addLength(str) {
  const output = [];
  for (let word of str.split(" ")) {
    output.push(`${word} ${word.length}`);
  }
  return output;
}
