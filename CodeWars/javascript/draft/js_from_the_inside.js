// https://www.codewars.com/kata/55afe435d2ce100356000032/train/javascript

Array.prototype.filter = function (callback, thisArg) {
  const output = [];
  const originalArray = this;
  const originalLength = originalArray.length;

  for (let i = 0; i < originalLength; i++) {
    if (callback.call(thisArg, originalArray[i], i, originalArray)) {
      output.push(originalArray[i]);
    }
  }
  return output;
};
