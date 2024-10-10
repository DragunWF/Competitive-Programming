// https://www.codewars.com/kata/57e1e61ba396b3727c000251/train/javascript

function stringClean(s) {
  const digits = "0123456789";
  let output = "";
  for (let char of s) {
    if (!digits.includes(char)) {
      output += char;
    }
  }
  return output;
}
