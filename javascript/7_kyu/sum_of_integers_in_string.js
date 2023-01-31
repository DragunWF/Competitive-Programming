// https://www.codewars.com/kata/598f76a44f613e0e0b000026/train/javascript

function sumOfIntegersInString(string) {
  const digits = "0123456789";
  let currentNum = [];
  let sum = 0;
  for (let i = 0; i < string.length; i++) {
    if (digits.includes(string[i])) {
      currentNum.push(string[i]);
      if (i + 1 === string.length) {
        sum += convertNumArr(currentNum);
      }
    } else {
      sum += convertNumArr(currentNum);
      currentNum = [];
    }
  }
  return sum;
}

function convertNumArr(arr) {
  return Number(arr.join(""));
}

// Not part of the solution
function test() {
  const testCases = [
    {
      testCase: "The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog",
      expected: 3635,
    },
    {
      testCase: "h3ll0w0rld",
      expected: 3,
    },
    {
      testCase: "2 + 3",
      expected: 5,
    },
    {
      testCase: "The Great Depression lasted from 1929 to 1939.",
      expected: 3868,
    },
  ];
  for (let i = 0; i < testCases.length; i++) {
    const result = sumOfIntegersInString(testCases[i].testCase);
    const correct = result === testCases[i].expected;
    console.log(`Test Case #${i + 1}: ${correct}`);
    if (!correct) {
      console.log("Failed Case:", `${result} != ${testCases[i].expected}`);
    }
  }
}

test();
