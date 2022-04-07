// https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/javascript

function calculate(firstNumber, secondNumber, operation) {
  return Math.floor(eval(`${firstNumber}${operation}${secondNumber}`));
}

function zero(operator = null) {
  if (!operator) return 0;
  return calculate(0, operator[1], operator[0]);
}

function one(operator = null) {
  if (!operator) return 1;
  return calculate(1, operator[1], operator[0]);
}

function two(operator = null) {
  if (!operator) return 2;
  return calculate(2, operator[1], operator[0]);
}

function three(operator = null) {
  if (!operator) return 3;
  return calculate(3, operator[1], operator[0]);
}

function four(operator = null) {
  if (!operator) return 4;
  return calculate(4, operator[1], operator[0]);
}

function five(operator = null) {
  if (!operator) return 5;
  return calculate(5, operator[1], operator[0]);
}

function six(operator = null) {
  if (!operator) return 6;
  return calculate(6, operator[1], operator[0]);
}

function seven(operator = null) {
  if (!operator) return 7;
  return calculate(7, operator[1], operator[0]);
}

function eight(operator = null) {
  if (!operator) return 8;
  return calculate(8, operator[1], operator[0]);
}

function nine(operator = null) {
  if (!operator) return 9;
  return calculate(9, operator[1], operator[0]);
}

function plus(number) {
  return ["+", number];
}

function minus(number) {
  return ["-", number];
}

function times(number) {
  return ["*", number];
}

function dividedBy(number) {
  return ["/", number];
}

console.log(five(times(three())));

// I should have used a ternary operator on my number functions
