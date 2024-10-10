// https://www.codewars.com/kata/52449b062fb80683ec000024

function generateHashtag(str) {
  const alphabets = "abcdefghijklmnopqrstuvwxyz";
  let output = "#";
  let capitalize = true;

  for (let i = 0; i < str.length; i++) {
    if (str[i] === " ") {
      capitalize = true;
      continue;
    }
    if (alphabets.includes(str[i].toLowerCase())) {
      output += capitalize ? str[i].toUpperCase() : str[i];
      capitalize = false;
    }
  }

  return output.length - 1 && output.length <= 140 ? output : false;
}

// Not part of the solution
function test() {
  const testCases = [
    " ",
    "",
    "Codewars",
    "Do we have A Hashtag?",
    "code" + " ".repeat(140) + "wars",
  ];
  for (let i = 0; i < testCases.length; i++) {
    const result = generateHashtag(testCases[i]);
    console.log(`Test Case #${i + 1}: ${result}`);
  }
}

test();
