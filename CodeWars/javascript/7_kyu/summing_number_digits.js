// https://www.codewars.com/kata/52f3149496de55aded000410/train/javascript

function sumDigits(number) {
  let sum = 0;
  for (let char of number.toString()) {
    if (char === "-") continue;
    sum += parseInt(char);
  }
  return sum;
}
