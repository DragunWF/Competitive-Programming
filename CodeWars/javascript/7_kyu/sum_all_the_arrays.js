// https://www.codewars.com/kata/5594463eaf1701909c0000d4/train/javascript

function arraySum(arr) {
  if (!arr) return 0;

  let totalSum = 0;
  function helper(item) {
    for (let element of item) {
      if (typeof element === "number") {
        totalSum += element;
      } else if (Array.isArray(element)) {
        helper(element);
      }
    }
  }
  helper(arr);
  return totalSum;
}

class TestCase {
  constructor(arr, expected) {
    this.arr = arr;
    this.expected = expected;
  }
}

function test() {
  const testCases = [
    new TestCase([1, 2], 3),
    new TestCase([1, 2, 3], 6),
    new TestCase([1, 2, [1, 2]], 6),
    new TestCase([1, 2, 3.5], 6.5),
    new TestCase([1, 2, "pig", 3], 6),
    new TestCase(
      [
        1,
        2,
        function () {
          return 15;
        },
        3,
      ],
      6,
    ),
    new TestCase([1, 2, [1, 2, 3, [5, 1, 0]]], 15),
    new TestCase(
      [
        1,
        2,
        [
          1,
          "pig",
          2,
          3,
          function () {
            return 15;
          },
          [5, 1, 0],
        ],
      ],
      15,
    ),
  ];

  let correctCount = 0;
  let currentIteration = 1;
  for (let testCase of testCases) {
    const result = arraySum(testCase.arr);
    const isCorrect = result === testCase.expected;
    if (isCorrect) {
      correctCount++;
    }
    console.log(
      `\nTest Case #${currentIteration}: ${isCorrect ? "Pass" : "Fail"}`,
    );
    console.log(`Actual: ${result}`);
    console.log(`Expected: ${testCase.expected}\n`);
    currentIteration++;
  }
  console.log(`Test Cases Passed: ${correctCount}/${testCases.length}`);
}

test();
