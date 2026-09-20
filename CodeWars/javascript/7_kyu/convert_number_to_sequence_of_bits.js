// https://www.codewars.com/kata/56536e45bd4717003a000056/train/javascript

Number.prototype.toBits = function (length = 8) {
  return padNum(length, this);
};

function padNum(minLength, num) {
  const strNum = num.toString(2);
  const padCount = minLength - strNum.length;
  let output = [];
  for (let i = 0; i < padCount; i++) {
    output.push("0");
  }
  output.push(strNum);
  return output.join("");
}
