// https://www.codewars.com/kata/57238ceaef9008adc7000603/train/javascript

function colorOf(r, g, b) {
  return `#${hex(r)}${hex(g)}${hex(b)}`;
}

function hex(n) {
  return n < 16 ? `0${n.toString(16)}` : n.toString(16);
}

function test() {
  // Not part of the solution, just testing
  console.log(colorOf(255, 0, 0)); // #ff0000
  console.log(colorOf(13, 29, 141)); // #0d1d8d
}

test();
