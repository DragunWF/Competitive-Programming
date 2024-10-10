// https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/javascript

function openOrSenior(data) {
  const output = [];
  for (let info of data) {
    output.push(info[0] >= 55 && info[1] > 7 ? "Senior" : "Open");
  }
  return output;
}
