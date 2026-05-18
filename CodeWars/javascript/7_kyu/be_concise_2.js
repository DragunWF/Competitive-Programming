// https://www.codewars.com/kata/56f4f7cfaf5b1f8cd100060e/train/javascript

function squaresOnly(a) {
  return a.filter(n => Number.isInteger(Math.sqrt(n)));
}

function squaresOnlyOld(array) {
  var result = [],
    isSquare;
  for (let i = 0; i < array.length; i++) {
    isSquare = !1; // !1 evaluates to false and is therefore a shorthand way of typing 'false'
    for (let k = 0; k <= 10; k++) {
      if (k ** 2 === array[i]) {
        isSquare = true;
      }
    }
    if (isSquare) {
      result[result.length] = array[i];
    }
  }
  return result;
}
