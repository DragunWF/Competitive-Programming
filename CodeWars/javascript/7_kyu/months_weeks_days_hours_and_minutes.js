// https://www.codewars.com/kata/5b2a10fe9e40b9b43d00008c/train/javascript

function displayValue(value) {
  const output = [];

  const minutes = value % 60;
  if (minutes > 0)
    output.unshift(`${minutes} ${minutes === 1 ? "minute" : "minutes"}`);
  const hours = Math.floor(value / 60) % 24;
  if (hours > 0) output.unshift(`${hours} ${hours === 1 ? "hour" : "hours"}`);
  const days = Math.floor(value / 60 / 24) % 7;
  if (days > 0) output.unshift(`${days} ${days === 1 ? "day" : "days"}`);
  const weeks = Math.floor(value / 60 / 24 / 7) % 4;
  if (weeks > 0) output.unshift(`${weeks} ${weeks === 1 ? "week" : "weeks"}`);
  const months = Math.floor(value / 60 / 24 / 7 / 4) % 12;
  if (months > 0)
    output.unshift(`${months} ${months === 1 ? "month" : "months"}`);
  const years = Math.floor(value / 60 / 24 / 7 / 28 / 12);
  if (years > 0) output.unshift(`${years} ${years === 1 ? "year" : "years"}`);

  return output.join(" ");
}

function test() {
  const testCases = [
    { data: 1, expected: "1 minute" },
    { data: 100, expected: "1 hour 40 minutes" },
    { data: 40321, expected: "1 month 1 minute" },
    { data: 52874, expected: "1 month 1 week 1 day 17 hours 14 minutes" },
  ];
  let nth = 1;
  let passes = 0;
  for (let testCase of testCases) {
    const result = displayValue(testCase.data);
    const isPassed = result === testCase.expected;
    if (isPassed) passes++;
    console.log(`
Test Case #${nth}: ${isPassed ? "Passed" : "Failed"}
Result: ${result}
Expected: ${testCase.expected}`);
    nth++;
  }
  console.log(`\nSummary: ${passes} out of ${testCases.length} passed!\n`);
}

test();
