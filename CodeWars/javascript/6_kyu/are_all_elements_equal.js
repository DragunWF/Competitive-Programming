// https://www.codewars.com/kata/5963caa2cb97be79630000c0/train/javascript

Object.defineProperty(String.prototype, "eqAll", {
  value: function eqAll() {
    return isAllEqual(this);
  },
});

Object.defineProperty(Array.prototype, "eqAll", {
  value: function eqAll() {
    return isAllEqual(this);
  },
});

function isAllEqual(iterable) {
  if (!iterable) {
    return true;
  }
  const anchor = iterable[0];
  for (let i = 1; i < iterable.length; i++) {
    if (anchor !== iterable[i]) {
      return false;
    }
  }
  return true;
}
