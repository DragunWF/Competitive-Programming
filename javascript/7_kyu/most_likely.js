// https://www.codewars.com/kata/56644a421b7c94c622000056/train/javascript

function mostLikely(prob1, prob2) {
  return toPercent(prob1) > toPercent(prob2);
}

function toPercent(prob) {
  const nums = prob.split(":");
  return Number(nums[0]) / Number(nums[1]);
}
