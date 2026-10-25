// https://www.codewars.com/kata/585a033e3a36cdc50a00011c/train/javascript

function freqSeq(str, sep) {
  const counter = createCounter(str);
  const freqChars = [];
  for (let char of str) {
    freqChars.push(String(counter[char]));
  }
  return freqChars.join(sep);
}

function createCounter(str) {
  const counter = {};
  for (let char of str) {
    if (char in counter) {
      counter[char]++;
    } else {
      counter[char] = 1;
    }
  }
  return counter;
}

class TestCase {
  constructor(str, sep, expected) {
    this.str = str;
    this.sep = sep;
    this.expected = expected;
  }
}

function test() {
  const testCases = [
    new TestCase("hello world", "-", "1-1-3-3-2-1-1-2-1-3-1"),
    new TestCase("19999999", ":", "1:7:7:7:7:7:7:7"),
    new TestCase("^^^**$", "x", "3x3x3x2x2x1"),
  ];
  let correctCount = 0;
  let testCaseCount = 1;
  for (let testCase of testCases) {
    const result = freqSeq(testCase.str, testCase.sep);
    const isCorrect = result === testCase.expected;
    if (isCorrect) {
      correctCount++;
    }
    console.log(
      `\nTest Case #${testCaseCount}: ${isCorrect ? "Pass" : "Fail"}`,
    );
    console.log(`Input: ${testCase.str} ${testCase.sep}`);
    console.log(`Actual: ${result}`);
    console.log(`Expected: ${testCase.expected}\n`);
  }
  console.log(`Test Cases Passed: ${correctCount}/${testCases.length}`);
}

test();
