// https://www.codewars.com/kata/52597aa56021e91c93000cb0

var moveZeros = function (arr) {
  let zero_count = 0;
  while (arr.includes(0)) {
    arr.splice(arr.indexOf(0), 1);
    zero_count++;
  }
  for (let i = 1; i <= zero_count; i++) arr.push(0);
  return arr;
};
