// https://www.codewars.com/kata/56a5d994ac971f1ac500003e

function longestConsec(strarr, k) {
  let output = "";
  for (let i = 0; i < strarr.length - k + 1; i++) {
    let currentStr = "";
    for (let j = 0; j < k; j++) {
      currentStr += strarr[j + i];
    }
    if (currentStr.length > output.length) {
      output = currentStr;
    }
  }
  return output;
}

// Not part of the solution
function test() {
  const testCases = [
    [["zone", "abigail", "theta", "form", "libe", "zas"], 2],
    [
      [
        "ejjjjmmtthh",
        "zxxuueeg",
        "aanlljrrrxx",
        "dqqqaaabbb",
        "oocccffuucccjjjkkkjyyyeehh",
      ],
      1,
    ],
    [
      [
        "itvayloxrp",
        "wkppqsztdkmvcuwvereiupccauycnjutlv",
        "vweqilsfytihvrzlaodfixoyxvyuyvgpck",
      ],
      2,
    ],
    [[], 3],
  ];
  for (let i = 0; i < testCases.length; i++) {
    const result = longestConsec(testCases[i][0], testCases[i][1]);
    console.log(`Test Case #${i + 1}: ${result}`);
  }
}

test();
