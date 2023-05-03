// https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/train/javascript

function findNeedle(haystack) {
  return `found the needle at position ${haystack.indexOf("needle")}`;
}

// Not part of the solution
function test() {
  const testCases = [
    ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"],
    [
      "3",
      "123124234",
      undefined,
      "needle",
      "world",
      "hay",
      2,
      "3",
      true,
      false,
    ],
  ];
  for (let i = 0; i < testCases.length; i++) {
    const result = findNeedle(testCases[i]);
    console.log(`Test Case #${i + 1}: ${result}`);
  }
}

test();
