// https://www.codewars.com/kata/5949481f86420f59480000e7

function oddOrEven(array) {
  if (array.length < 1) return "even";
  let sum = array.reduce((a, b) => {
    return a + b;
  });
  return sum % 2 ? "odd" : "even";
}
