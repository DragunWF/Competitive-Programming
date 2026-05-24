// https://www.codewars.com/kata/57a83e447cb1f32de80000d5/train/javascript

function lenR(arr) {
  function countHelper(arr, index = 0) {
    if (arr[index]) {
      return countHelper(arr, index + 1);
    }
    return index;
  }
  return countHelper(arr);
}
