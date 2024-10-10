// https://www.codewars.com/kata/569d488d61b812a0f7000015/train/javascript

function dataReverse(data) {
  const output = [];
  let byte = "";
  for (let i = 0; i < data.length; i++) {
    byte += data[i].toString();
    if ((i + 1) % 8 == 0) {
      output.push(byte);
      byte = "";
    }
  }
  output.reverse();
  return output.join("").split("").map(n => Number(n));
}
