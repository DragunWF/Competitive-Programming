// https://www.codewars.com/kata/57ea5b0b75ae11d1e800006c/train/javascript

function sortByLength(array) {
  return array.sort((a, b) => a.length - b.length);
}

// Not part of the solution, just testing
function test() {
  const values = ["Telescopes", "Glasses", "Eyes", "Monocles"];
  console.log(sortByLength(values));
}

test();
