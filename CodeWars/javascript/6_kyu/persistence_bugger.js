// https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec

function persistence(num) {
  let loopCount = 0;
  while (num > 9) {
    num = eval(num.toString().split("").join("*"));
    loopCount++;
  }
  return loopCount;
}
