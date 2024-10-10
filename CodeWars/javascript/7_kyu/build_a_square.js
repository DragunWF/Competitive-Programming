// https://www.codewars.com/kata/59a96d71dbe3b06c0200009c/train/javascript

function generateShape(integer) {
  const output = [];
  for (let i = 0; i < integer; i++) {
    let line = "";
    for (let j = 0; j < integer; j++) line += "+";
    output.push(line);
  }
  return output.join("\n");
}
