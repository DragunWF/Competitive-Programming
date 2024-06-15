// https://www.codewars.com/kata/52a112d9488f506ae7000b95/train/javascript

function isIntArray(arr) {
  if (typeof arr !== "object" || arr === null) return false;
  for (let item of arr) {
    if (!Number.isInteger(item)) {
      return false;
    }
  }
  return true;
}

// Not part of the solution, just testing
function test() {
  console.log(Number.isInteger(1.5));
  console.log(Number.isInteger(1));
  console.log(typeof []);
  console.log(isIntArray(1.5));
  console.log(isIntArray(null));
}

test();
