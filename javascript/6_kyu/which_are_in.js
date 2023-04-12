// https://www.codewars.com/kata/550554fd08b86f84fe000a58

function inArray(array1, array2) {
  const output = [];
  for (let subStr of array1) {
    for (let str of array2) {
      if (str.includes(subStr)) {
        output.push(subStr);
        break;
      }
    }
  }
  output.sort();
  return output;
}

// Not part of the solution
function test() {
  const testCases = [
    [
      ["arp", "live", "strong"],
      ["lively", "alive", "harp", "sharp", "armstrong"],
    ],
    [
      ["tarp", "mice", "bull"],
      ["lively", "alive", "harp", "sharp", "armstrong"],
    ],
  ];
  for (let i = 0; i < testCases.length; i++) {
    const result = inArray(testCases[i][0], testCases[i][1]);
    console.log(`Test Case #${i + 1}: [${result}]`);
  }
}

test();
