// https://www.codewars.com/kata/583203e6eb35d7980400002a/train/javascript

function countSmileys(arr) {
  let smileys = 0;
  for (let face of arr) {
    if (face.length === 3 && !face.includes("-") && !face.includes("~")) {
      continue;
    }
    if (
      (face.includes(":") || face.includes(";")) &&
      (face.includes(")") || face.includes("D")) &&
      face.length <= 3
    ) {
      smileys++;
    }
  }
  return smileys;
}

// Not part of the solution
function test() {
  const testCases = [
    [":)", ";(", ";}", ":-D"],
    [";D", ":-(", ":-)", ";~)"],
    [";]", ":[", ";*", ":$", ";-D"],
    [";(", ":oD", ";)", ";)", ":)", ":o)", ":D"],
    [":---)", "))", ";~~D", ";D"],
  ];
  for (let i = 0; i < testCases.length; i++) {
    const result = countSmileys(testCases[i]);
    console.log(`Test Case #${i + 1}: ${result}`);
  }
}

test();
