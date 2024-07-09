// https://www.codewars.com/kata/5728203b7fc662a4c4000ef3/train/javascript

function alienLanguage(str) {
  const words = str.split(" ");
  const output = [];
  for (let word of words) {
    output.push(
      word.substring(0, word.length - 1).toUpperCase() +
        word.charAt(word.length - 1).toLowerCase()
    );
  }
  return output.join(" ");
}

function test() {
  // Not part of the solution, just testing
  console.log(alienLanguage("My name is John"));
}

test();
