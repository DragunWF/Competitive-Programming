// https://www.codewars.com/kata/529f2d1c403a58f660000656

var Calculator = {
  add: function (a, b) {
    return a + b;
  },
  subtract: function (a, b) {
    return a - b;
  },
  multiply: function (a, b) {
    return a * b;
  },
  divide: function (a, b) {
    if (!a || !b) return false;
    return a / b;
  },
};
