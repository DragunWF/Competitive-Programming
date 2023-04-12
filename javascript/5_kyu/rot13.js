// Same solution for both of these katas
// https://codewars.com/kata/530e15517bc88ac656000716
// https://www.codewars.com/kata/52223df9e8f98c7aa7000062

function rot13(message) {
  let output = "";
  const alphabets = "abcdefghijklmnopqrstuvwxyz";
  for (let char of message) {
    if (alphabets.includes(char.toLowerCase())) {
      const index =
        (alphabets.indexOf(char.toLowerCase()) + 13) % alphabets.length;
      output +=
        char.toLowerCase() === char
          ? alphabets[index]
          : alphabets[index].toUpperCase();
      continue;
    }
    output += char;
  }
  return output;
}

// Not part of the solution
function test() {
  const testCases = ["Test", "Grfg", "zZxXyY"];
  for (let i = 0; i < testCases.length; i++) {
    const result = rot13(testCases[i]);
    console.log(`Test Case #${i + 1}: ${result}`);
  }
}

test();
