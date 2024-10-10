// https://www.codewars.com/kata/57274562c8dcebe77e001012/train/javascript

function cutIt(arr) {
  const minLength = Math.min(...arr.map((item) => item.length));
  const output = [];
  for (let item of arr) {
    output.push(item.substring(0, minLength));
  }
  return output;
}

// Not part of the solution, just testing
function test() {
  console.log(cutIt(["ab", "cde", "fgh"]));
}

test();
