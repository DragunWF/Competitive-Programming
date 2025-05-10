// https://www.codewars.com/kata/54fb853b2c8785dd5e000957/train/javascript

function chain(input, fs) {
  for (let func of fs) {
    input = func(input);
  }
  return input;
}
