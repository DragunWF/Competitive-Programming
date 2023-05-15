// https://www.codewars.com/kata/58f5c63f1e26ecda7e000029

function wave(str) {
  const output = [];
  for (let i = 0; i < str.length; i++) {
    if (str[i] === " ") {
      continue;
    }
    let item = str.split("");y
    item[i] = item[i].toUpperCase();
    output.push(item.join(""));
  }
  return output;
}

// Not part of the solution
function test() {
  const testCases = ["hello", "codewars", "gap"];
  for (let i = 0; i < testCases.length; i++) {
    const result = wave(testCases[i]);
    console.log(`Test Case #${i + 1}: [${result}]`);
  }
}

test();
