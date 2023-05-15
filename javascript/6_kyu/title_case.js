// https://www.codewars.com/kata/5202ef17a402dd033c000009/train/javascript

function titleCase(title, minorWords) {
  if (!title) {
    return "";
  }
  const output = [];
  minorWords = minorWords ? minorWords.toLowerCase().split(" ") : [];
  title = title.split(" ");
  for (let i = 0; i < title.length; i++) {
    if (minorWords.includes(title[i].toLowerCase()) && i !== 0) {
      output.push(title[i].toLowerCase());
      continue;
    }
    output.push(
      `${title[i][0].toUpperCase()}${title[i].substring(1).toLowerCase()}`
    );
  }
  return output.join(" ");
}

// Not part of the solution
function test() {
  const testCases = [
    ["a clash of KINGS", "a an the of"],
    ["THE WIND IN THE WILLOWS", "The In"],
    ["the quick brown fox"],
  ];
  for (let i = 0; i < testCases.length; i++) {
    const result = titleCase(testCases[i][0], testCases[i][1]);
    console.log(`Test Case #${i + 1}: ${result}`);
  }
}

test();
