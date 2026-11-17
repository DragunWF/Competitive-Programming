// https://www.codewars.com/kata/57fb79784e2d0639c9000066/train/javascript

function sortItOut(array) {
  const evenNums = [];
  const oddNums = [];
  for (let num of array) {
    const normalizedNum = Math.floor(num);
    if (normalizedNum % 2 === 0) {
      evenNums.push(num);
    } else {
      oddNums.push(num);
    }
  }
  evenNums.sort((a, b) => b - a);
  oddNums.sort((a, b) => a - b);
  return [...oddNums, ...evenNums];
}
