// https://www.codewars.com/kata/581351c40d8f13bc450008b8/train/javascript

Array.prototype.first = function () {
  return this[0];
};

Array.prototype.last = function () {
  return this[this.length - 1];
};
