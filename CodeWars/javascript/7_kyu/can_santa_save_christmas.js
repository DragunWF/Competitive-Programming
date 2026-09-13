// https://www.codewars.com/kata/5857e8bb9948644aa1000246/train/javascript

function determineTime(durations) {
  if (!durations.length) {
    return true;
  }
  let seconds = 0;
  let minutes = 0;
  let hours = 0;
  for (let duration of durations) {
    const values = duration.split(":");
    seconds += parseInt(values[2]);
    minutes += parseInt(values[1]);
    hours += parseInt(values[0]);
  }

  let secondsToHours = seconds / 60 / 60;
  let minutesToHours = minutes / 60;
  return secondsToHours + minutesToHours + hours <= 24;
}

class TestCase {
  constructor(durations, expected) {
    this.durations = durations;
    this.expected = expected;
  }
}

function test() {
  const testCases = [
    new TestCase(["00:30:00", "02:30:00", "00:15:00"], true),
    new TestCase([], true),
    new TestCase(["04:30:00", "02:00:00", "01:30:00", "16:00:00"], true),
    new TestCase(["12:00:00", "12:00:00"], true),
    new TestCase(["12:00:00", "12:00:01"], false),
    new TestCase(["06:00:00", "12:00:00", "06:30:00"], false),
  ];
  let correctCount = 0;
  let testCaseCount = 1;
  for (let testCase of testCases) {
    const result = determineTime(testCase.durations);
    const isCorrect = result === testCase.expected;
    if (isCorrect) {
      correctCount++;
    }
    console.log(
      `Test Case #${testCaseCount}: ${isCorrect ? "Passed" : "Failed"}`,
    );
    console.log(`Input: ${testCase.durations}`);
    console.log(`Actual: ${result}`);
    console.log(`Expected: ${testCase.expected}`);

    testCaseCount++;
  }
  console.log(`Test Cases Passed #${correctCount}/${testCases.length}`);
}

test();
