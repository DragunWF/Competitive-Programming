// https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/javascript

function sumIntervals(intervals) {
  if (intervals.length == 1) return intervals[0][1] - intervals[0][0];

  intervals.sort((a, b) => a[0] - b[0]);
  const newIntervals = [];
  let numPair = [intervals[0][0], intervals[0][1]];
  for (let i = 1; i < intervals.length; i++) {
    if (numPair[1] > intervals[i][0]) {
      numPair[1] = numPair[1] > intervals[i][1] ? numPair[1] : intervals[i][1];
    } else {
      newIntervals.push([...numPair]);
      numPair[0] = intervals[i][0];
      numPair[1] = intervals[i][1];
    }
    if (i + 1 == intervals.length) newIntervals.push(numPair);
  }

  return newIntervals.reduce((a, b) => a + b[1] - b[0], 0);
}

console.log(
  sumIntervals([
    [1, 5],
    [10, 20],
    [1, 6],
    [16, 19],
    [5, 11],
  ])
); // => 19

console.log(
  sumIntervals([
    [1, 2],
    [6, 10],
    [11, 15],
  ])
); // => 9

console.log(
  sumIntervals([
    [1, 4],
    [7, 10],
    [3, 5],
  ])
); // => 7
