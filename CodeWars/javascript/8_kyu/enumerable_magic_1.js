// https://www.codewars.com/kata/54598d1fcbae2ae05200112c/train/javascript

function all(arr, fun) {
  for (let item of arr) if (!fun(item)) return false;
  return true;
}
