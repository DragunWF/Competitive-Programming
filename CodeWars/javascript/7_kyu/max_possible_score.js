// https://www.codewars.com/kata/59656c69253c365e58000046/train/javascript

function maxPossibleScore(obj, arr) {
  let score = 0;
  for (let key in obj) {
    score += arr.includes(key) ? obj[key] * 2 : obj[key];
  }
  return score;
}
