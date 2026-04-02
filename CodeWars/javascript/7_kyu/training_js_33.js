// https://www.codewars.com/kata/5733d6c2d780e20173000baa

function maxMin(arr1, arr2) {
  const diffArr = [];
  for (let i = 0; i < arr1.length; i++) {
    diffArr.push(Math.abs(arr1[i] - arr2[i]));
  }
  return [Math.max(...diffArr), Math.min(...diffArr)];
}
