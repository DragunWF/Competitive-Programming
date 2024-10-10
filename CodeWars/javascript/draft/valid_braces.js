// https://www.codewars.com/kata/5277c8a221e209d3f6000b56/train/javascript

class Brace {
  constructor(openingBrace, closingBrace) {
    this.variations = [openingBrace, closingBrace];
    this.openingBrace = openingBrace;
    this.closingBrace = closingBrace;
    this.pos = 0;
  }

  updatePos(brace) {
    if (brace === this.openingBrace) this.pos++;
    else if (brace === this.closingBrace) this.pos--;
  }
}

function validBraces(bracesString) {
  const braces = [
    new Brace("[", "]"),
    new Brace("{", "}"),
    new Brace("(", ")"),
  ];
  for (let character of bracesString) {
    for (let i = 0; i < braces.length; i++) {
      if (braces[i].variations.includes(character)) {
        braces[i].updatePos(character);
        // if (!checkBalance(braces, i)) {
        //   return false;
        // }
        break;
      }
    }
  }
  return checkBalance(braces);
}

function checkBalance(braces, exceptionIndex = null) {
  for (let i = 0; i < braces.length; i++) {
    if (exceptionIndex !== i && braces[i].pos !== 0) {
      return false;
    }
  }
  return true;
}

// Not part of the solution
function test() {
  const testCases = [
    { sample: "()", expected: true },
    { sample: "[]", expected: true },
    { sample: "{}", expected: true },
    { sample: "([{}])", expected: true },
    { sample: "[(])", expected: false },
    { sample: "(}", expected: false },
    { sample: "[({})](]", expected: false },
  ];
  for (let i = 0; i < testCases.length; i++) {
    const result = validBraces(testCases[i].sample);
    const correct = result === testCases[i].expected;
    console.log(`Test Case #${i + 1}: ${result}`);
    if (!correct) {
      console.log(
        `Failed Case: Got "${result}", expected "${testCases[i].expected}"`
      );
    }
  }
}

test();
