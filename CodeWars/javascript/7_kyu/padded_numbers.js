// https://www.codewars.com/kata/5d50e3914861a500121e1958/train/java

function solution(value) {
  const len = value.toString().length;
  let zeroes = "";
  for (let i = 0; i < 5 - len; i++) {
    zeroes += "0";
  }
  return `Value is ${zeroes}${value}`;
}
