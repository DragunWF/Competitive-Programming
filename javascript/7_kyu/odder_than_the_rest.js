// https://www.codewars.com/kata/5983cba828b2f1fd55000114/train/javascript

function oddOne(arr) {
  let index = -1;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 !== 0) {
      index = i;
      break;
    }
  }
  return index;
}
