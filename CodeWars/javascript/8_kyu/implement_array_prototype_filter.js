// https://www.codewars.com/kata/56dd9b84fe5754786f0014f7/train/javascript

Array.prototype.filter = function (func) {
  const output = [];
  for (let item of this) {
    if (func(item)) {
      output.push(item);
    }
  }

  this.length = 0;
  this.push(...output);
  return output;
};
