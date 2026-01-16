// https://www.codewars.com/kata/56035d75426e197c3e0000a2/train/javascript

Array.prototype.remove = function (pred) {
  const removed = [];
  const current = [];
  for (let i = 0; i < this.length; i++) {
    if (pred(this[i])) {
      removed.push(this[i]);
    } else {
      current.push(this[i]);
    }
  }
  this.length = 0;
  for (let item of current) {
    this.push(item);
  }
  return removed;
};
