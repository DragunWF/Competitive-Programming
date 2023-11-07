// https://www.codewars.com/kata/525d50d2037b7acd6e000534/train/javascript

const test = [1, 2, 3, 4, 5];

Array.prototype.square = function () {
  return this.map((n) => n * n);
};

Array.prototype.cube = function () {
  return this.map((n) => n * n * n);
};

Array.prototype.sum = function () {
  return this.reduce((a, b) => a + b);
};

Array.prototype.average = function () {
  if (!this.length) return NaN;
  return this.sum() / this.length;
};

Array.prototype.even = function () {
  return this.filter((n) => n % 2 === 0);
};

Array.prototype.odd = function () {
  return this.filter((n) => n % 2 !== 0);
};

console.log(test.square());
