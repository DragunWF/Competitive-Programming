// https://www.codewars.com/kata/5411e3e95f3a7f6a7a0000e3/train/javascript

Array.prototype.reduce = function (process, initial) {
  let endResult = initial ? initial : this[0];
  for (let i = Number(!Boolean(initial)); i < this.length; i++) {
    endResult = process(endResult, this[i]);
  }
  return endResult;
};

// Not part of the solution, just testing
function test() {
  console.log([9, 3, 1].reduce((x, y) => x + y, 2));
  console.log([9, 3, 1].reduce((x, y) => x + y));
}

test();
