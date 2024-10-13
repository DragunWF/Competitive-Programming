// https://www.codewars.com/kata/527a6e602a7db3456e000a2b/train/javascript

Object.prototype.hash = function (path) {
  const keys = path.split(".");
  let currentValue = null;
  for (let key of keys) {
    if (
      (!currentValue && this.hasOwnProperty(key)) ||
      (currentValue && currentValue.hasOwnProperty(key))
    ) {
      currentValue = currentValue === null ? this[key] : currentValue[key];
    } else {
      return undefined;
    }
  }
  return currentValue;
};
