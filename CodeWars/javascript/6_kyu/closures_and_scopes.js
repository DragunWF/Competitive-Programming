// https://www.codewars.com/kata/526ec46d6f5e255e150002d1/train/javascript

function createFunctions(n) {
  let callbacks = [];
  for (let i = 0; i < n; i++) {
    callbacks.push(() => i);
  }
  return callbacks;
}
