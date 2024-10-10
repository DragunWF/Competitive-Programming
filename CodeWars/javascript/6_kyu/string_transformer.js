// https://www.codewars.com/kata/5878520d52628a092f0002d0/train/javascript

function stringTransformer(str) {
  const words = str.split(" ");
  let output = [];
  for (let i = words.length - 1; i >= 0; i--) {
    let word = "";
    for (let char of words[i]) {
      word += char === char.toUpperCase() ? 
        char.toLowerCase() : char.toUpperCase();
    }
    output.push(word);
  }
  return output.join(" ");
}

// Not part of the solution, just testing
function test() {
  console.log(stringTransformer("Example string"));
}

test();
