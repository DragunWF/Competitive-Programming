// https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/javascript

function solution(list) {
  let rangeNum = null;
  let hasRange = false;
  let numsInRange = 0;
  const output = [];

  for (let i = 0; i < list.length; i++) {
    const sum = list[i] + 1;
    const nextNum = list[i + 1];
    if (hasRange) numsInRange++;
    if (nextNum != sum) {
      if (hasRange && numsInRange > 2) output.push(`${rangeNum}-${list[i]}`);
      else if (hasRange && numsInRange <= 2) {
        output.push(list[i - 1]);
        output.push(list[i]);
      } else output.push(list[i]);
      hasRange = false;
      numsInRange = 0;
    }
    if (nextNum == sum && !hasRange) {
      rangeNum = list[i];
      hasRange = true;
      numsInRange++;
    }
  }

  return output.join(",");
}

const result = solution([
  -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20,
]);
const correctAns = "-6,-3-1,3-5,7-11,14,15,17-20";
console.log(`${result}\n${correctAns}`);
console.log("=", result == correctAns);
