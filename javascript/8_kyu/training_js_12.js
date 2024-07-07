// https://www.codewars.com/kata/5722b3f0bd5583cf44001000/train/javascript

function giveMeFive(obj) {
  const output = [];
  for (let key in obj) {
    if (key.length === 5) {
      output.push(key);
    }
    if (obj[key].length === 5) {
      output.push(obj[key]);
    }
  }
  return output;
}

function test() {
  // Not part of the solution
  console.log(giveMeFive({ Our: "earth", is: "a", beautyful: "world" }));
}

test();
