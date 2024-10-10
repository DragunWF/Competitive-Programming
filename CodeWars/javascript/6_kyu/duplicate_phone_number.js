// https://www.codewars.com/kata/58bf67eb68d8469e3c000041/train/javascript

function findDuplicatePhoneNumbers(phoneNumber) {
  const numbers = [];
  const alphabets = getAlphabets();

  for (let i = 0; i < phoneNumber.length; i++) {
    let number = "";
    for (let j = 0; j < phoneNumber[i].length; j++) {
      if (alphabets.includes(phoneNumber[i][j].toLowerCase())) {
        numbers.push(mapLetter(phoneNumber[i][j]));
      } else {
        numbers.push(phoneNumber[i][j]);
      }
    }
    numbers.push(number);
  }

  return numbers;
}

function getDuplicates(phoneNumbers) {
  const unique = [];
  const duplicates = [];
  for (let number of phoneNumbers) {
    if (!duplicates.includes(number)) {
      unique.push(number);
    } else {
      duplicates.push(number);
    }
  }
}

function getAlphabets() {
  return "abcdefghijklmnopqrstuvwxy".split("");
}

function mapLetter(letter) {
  const alphabets = getAlphabets();
  const index = alphabets.findIndex(letter.toLowerCase())
  return Math.ceil((index + 1) / 3);
}

// Not part of the solution
function test() {
  const testCases = [
    [
      "4873279",
      "ITS-EASY",
      "888-4567",
      "3-10-10-10",
      "888-GLOP",
      "TUT-GLOP",
      "967-11-11",
      "310-GINO",
      "F101010",
      "888-1200",
      "-4-8-7-3-2-7-9-",
      "487-3279",
    ],
  ];
  for (let i = 0; i < testCases.length; i++) {
    const nth = i + 1;
    const result = findDuplicatePhoneNumbers(testCases[i]);
    console.log(`Test Case #${nth}: ${result}`);
  }
}

test();
