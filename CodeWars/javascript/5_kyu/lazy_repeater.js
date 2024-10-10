// https://www.codewars.com/kata/51fc3beb41ecc97ee20000c3

function makeLooper(str) {
  let index = 0;
  function repeater() {
    index++;
    return str[(index - 1) % str.length];
  }
  return repeater;
}

// Not part of the solution
const abc = makeLooper("abc");
for (let i = 0; i < 3; i++) {
  console.log(abc());
}
