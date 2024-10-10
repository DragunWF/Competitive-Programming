// https://www.codewars.com/kata/51b6249c4612257ac0000005

function solution(roman) {
  let output = 0;
  let previousValue = null;
  const numerals = [
    { symbol: "I", value: 1 },
    { symbol: "V", value: 5 },
    { symbol: "X", value: 10 },
    { symbol: "L", value: 50 },
    { symbol: "C", value: 100 },
    { symbol: "D", value: 500 },
    { symbol: "M", value: 1000 },
  ];
  for (let i = 0; i < roman.length; i++) {
    for (let j = 0; j < numerals.length; j++) {
      if (roman[i] === numerals[j].symbol) {
        if (i > 0 && numerals[j].value > previousValue) {
          output -= previousValue * 2;
        }
        output += numerals[j].value;
        previousValue = numerals[j].value;
        break;
      }
    }
  }
  return output;
}

// Not part of the solution
function test() {
  const testCases = ["XXI", "IV", "V", "MMXLVIII"];
  for (let i = 0; i < testCases.length; i++) {
    const result = solution(testCases[i]);
    console.log(`Test Case #${i + 1}: ${result}`);
  }
}

test();
