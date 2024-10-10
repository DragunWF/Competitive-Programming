// https://www.codewars.com/kata/5511b2f550906349a70004e1/train/javascript

let lastDigit = function (str1, str2) {
  const number = String(BigInt(str1) ** BigInt(str2));
  return Number(number.charAt(number.length - 1));
};
