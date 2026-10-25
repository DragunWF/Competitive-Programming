// https://www.codewars.com/kata/5f8a15c06dbd530016be0c19/train/javascript

function duplicateSandwich(data) {
  const counter = createCounter(data);
  let firstDuplicateIndex = null;
  let secondDuplicateIndex = null;
  for (let i = 0; i < data.length; i++) {
    const isDuplicate = counter[data[i]] > 1;
    if (isDuplicate) {
      if (firstDuplicateIndex === null) {
        firstDuplicateIndex = i;
      } else {
        secondDuplicateIndex = i;
        break;
      }
    }
  }
  return data.slice(firstDuplicateIndex + 1, secondDuplicateIndex);
}

function duplicateSandwichOld(data) {
  let firstDuplicateIndex = null;
  let secondDuplicateIndex = null;
  const seen = [];
  for (let i = 0; i < data.length; i++) {
    if (!seen.includes(data[i])) {
      seen.push(data[i]);
    } else {
      if (firstDuplicateIndex === null) {
        firstDuplicateIndex = i;
      } else {
        secondDuplicateIndex = i;
        break;
      }
    }
  }
  return data.slice(firstDuplicateIndex, secondDuplicateIndex);
}

function createCounter(data) {
  const counter = {};
  for (let element of data) {
    if (element in counter) {
      counter[element]++;
    } else {
      counter[element] = 1;
    }
  }
  return counter;
}

function arrayEquals(arr1, arr2) {
  if (arr1.length !== arr2.length) {
    return false;
  }
  for (let i = 0; i < arr1.length; i++) {
    if (arr1[i] !== arr2[i]) {
      return false;
    }
  }
  return true;
}

class TestCase {
  constructor(data, expected) {
    this.data = data;
    this.expected = expected;
  }
}

function test() {
  const testCases = [
    new TestCase([0, 1, 2, 3, 4, 5, 6, 1, 7, 8], [2, 3, 4, 5, 6]),
    new TestCase(
      ["None", "Hello", "Example", "hello", "None", "Extra"],
      ["Hello", "Example", "hello"],
    ),
    new TestCase([0, 0], []),
    new TestCase([true, false, true], [false]),
    new TestCase("example", "xampl"),
  ];
  let correctCount = 0;
  let testCaseCount = 1;
  for (let item of testCases) {
    const result = duplicateSandwich(item.data);
    let isCorrect;
    if (typeof result === "string") {
      isCorrect = result === item.expected;
    } else {
      isCorrect = arrayEquals(result, item.expected);
    }
    if (isCorrect) {
      correctCount++;
    }
    console.log(
      `\nTest Case #${testCaseCount}: ${isCorrect ? "Pass" : "Fail"}`,
    );
    console.log(`Input: ${item.data}`);
    console.log(`Actual: ${result}`);
    console.log(`Expected: ${item.expected}\n`);
    testCaseCount++;
  }
  console.log(`Test Cases Passed: ${correctCount}/${testCases.length}`);
}

test();
