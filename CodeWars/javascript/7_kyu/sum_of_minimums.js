// https://www.codewars.com/kata/5d5ee4c35162d9001af7d699

function sumOfMinimums(matrix) {
  let sum = 0;
  for (let arr of matrix) {
    sum += Math.min(...arr);
  }
  return sum;
}
