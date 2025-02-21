// https://www.codewars.com/kata/545993ee52756d98ca0010e1/train/javascript

function none(arr, fun) {
  for (let item of arr) {
    if (fun(item)) {
      return false;
    }
  }
  return true;
}
