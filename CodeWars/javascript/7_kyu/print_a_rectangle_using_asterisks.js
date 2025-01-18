// https://www.codewars.com/kata/5937ae46377144bb2f000029/train/javascript

function getRectangleString(width, height) {
  const output = [];
  for (let i = 0; i < height; i++) {
    let line = "";
    for (let j = 0; j < width; j++) {
      if (i === 0 || i === height - 1) {
        line += "*";
      } else {
        line += j === 0 || j === width - 1 ? "*" : " ";
      }
    }
    output.push(line);
  }
  return output.join("\r\n") + "\r\n";
}

// Not part of the solution
function test() {
  console.log(getRectangleString(3, 3));
  console.log(getRectangleString(2, 2));
  console.log(getRectangleString(5, 7));
}

test();
