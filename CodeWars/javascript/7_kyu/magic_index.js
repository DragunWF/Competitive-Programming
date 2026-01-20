// https://www.codewars.com/kata/57d5fed61a6282bf6f002a5f/train/javascript

function findMagic(arr) {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === i) {
      return i;
    }
  }
  return -1;
}
