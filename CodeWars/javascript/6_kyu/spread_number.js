// https://www.codewars.com/kata/5cbded7a36240b000dac91eb/train/javascript

Number.prototype[Symbol.iterator] = function* () {
  const n = this.valueOf();
  for (let i = 1; i <= n; i++) {
    yield i;
  }
};
