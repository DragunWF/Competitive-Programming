// https://www.codewars.com/kata/59f7fc109f0e86d705000043/train/javascript

function divisibleByThree(str) {
  let total = 0;
  for (let digit of str) {
    total += parseInt(digit);
  }
  return total % 3 === 0;
}
