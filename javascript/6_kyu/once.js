// https://www.codewars.com/kata/5307ff5b588fe6d7000000a5/train/javascript

function once(fn) {
  let executed = false;
  return (...args) => {
    if (!executed) {
      executed = true;
      return fn(...args);
    }
  };
}

function test() {
  // Not part of the solution, just testing
  const logOnce = once(console.log);
  logOnce("foo"); // -> "foo"
  logOnce("bar"); // -> undefined
}

test();
