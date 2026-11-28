// https://www.codewars.com/kata/58e16de3a312d34d000000bd/train/javascript

function rankings(numbers) {
  console.log(numbers);
  const sortedNumbers = [...numbers];
  sortedNumbers.sort((a, b) => b - a);
  const rankedNumbers = [];
  for (let i = 0; i < numbers.length; i++) {
    rankedNumbers.push(sortedNumbers.indexOf(numbers[i]) + 1);
  }
  return rankedNumbers;
}

class TestCase {
  constructor(numbers, expected) {
    this.numbers = numbers;
    this.expected = expected;
  }
}

function test() {
  const testCases = [
    new TestCase([1, 3, 2], [3, 1, 2]),
    new TestCase([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    new TestCase([3, 4, 1, 2, 5], [3, 2, 5, 4, 1]),
    new TestCase([10, 20, 40, 50, 30], [5, 4, 2, 1, 3]),
    new TestCase([1, 10], [2, 1]),
    new TestCase(
      [22, 33, 18, 9, 110, 4, 1, 88, 6, 50],
      [5, 4, 6, 7, 1, 9, 10, 2, 8, 3],
    ),
  ];
  let correctCount = 0;
  for (let i = 0, nth = 1; i < testCases.length; i++, nth++) {
    const testCase = testCases[i];
    const result = rankings(testCase.numbers);
    const isCorrect = isArrayEqual(result, testCase.expected);
    if (isCorrect) {
      correctCount++;
    }
    console.log(`Test Case #${nth}: ${isCorrect ? "Passed" : "Failed"}`);
    console.log(`Input: ${testCase.numbers}`);
    console.log(`Actual: ${result}`);
    console.log(`Expected: ${testCase.expected}\n`);
  }
  console.log(`Test Cases Passed: ${correctCount}/${testCases.length}`);
}

function isArrayEqual(arrayOne, arrayTwo) {
  if (arrayOne.length !== arrayTwo.length) return false;
  for (let i = 0; i < arrayOne.length; i++) {
    if (arrayOne[i] !== arrayTwo[i]) {
      return false;
    }
  }
  return true;
}

test();
