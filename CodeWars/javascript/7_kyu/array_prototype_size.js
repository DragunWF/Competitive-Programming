// https://www.codewars.com/kata/58638bd2210be9a9690001f7/train/javascript

Array.prototype.size = function () {
  let length = 0;
  for (let item of this) {
    length++;
  }
  return length;
};
