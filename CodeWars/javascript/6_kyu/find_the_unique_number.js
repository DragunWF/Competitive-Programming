// https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/javascript

function findUniq(arr) {
  const set = [...new Set(arr)];
  return getCount(arr, set[0]) >= 2 ? set[1] : set[0];
}

function getCount(arr, element) {
  let count = 0;
  for (let item of arr) if (item === element) count++;
  return count;
}
