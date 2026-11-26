// https://www.codewars.com/kata/56aaf25213edd3a88a000002/train/javascript

Object.defineProperty(Array.prototype, "zip", {
  value: function zip(otherArray, mapFn) {
    const minLength = Math.min(this.length, otherArray.length);
    const output = [];
    for (let i = 0; i < minLength; i++) {
      output.push(mapFn(this[i], otherArray[i]));
    }
    return output;
  },
});
