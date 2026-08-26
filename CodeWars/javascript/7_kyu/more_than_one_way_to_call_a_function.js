// https://www.codewars.com/kata/547aadd5b84a1fd66800041e/train/javascript

function sum(a, b) {
  let firstNumber = a;
  const add = (num) => {
    return firstNumber + num;
  };
  if (b !== undefined) {
    return firstNumber + b;
  }
  return add;
}
