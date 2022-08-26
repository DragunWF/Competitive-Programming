// https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/javascript

function sumIntervals(intervals) {
  const nums = [];
  intervals.sort((a, b) => a[0] - b[0]);
  for (let pair of intervals) {
    for (let i = pair[0]; i <= pair[1]; i++) {
      if (!nums.includes(i)) nums.push(i);
    }
  }
  const intervalRanges = createIntervalRanges(nums);
  console.log(intervalRanges);
  return sumRanges(intervalRanges);
}

function createIntervalRanges(numArr) {
  const output = [];
  let range = [];
  for (let i = 0; i < numArr.length; i++) {
    range.push(numArr[i]);
    if (numArr[i + 1] != numArr[i] + 1) {
      output.push(range);
      range = [];
    }
  }
  return output;
}

function sumRanges(rangeArr) {
  let sum = 0;
  for (let range of rangeArr) sum += range.length - 1;
  return sum;
}
