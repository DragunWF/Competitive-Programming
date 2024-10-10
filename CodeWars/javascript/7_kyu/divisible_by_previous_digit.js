// https://www.codewars.com/kata/5a2809dbe1ce0e07f800004d/train/javascript

function divisibleByLast(n) {
  const output = [false];
  const strNum = n.toString();
  for (let i = 1; i < strNum.length; i++) {
    output.push(strNum[i] % parseInt(strNum[i - 1]) === 0);
  }
  return output;
}
