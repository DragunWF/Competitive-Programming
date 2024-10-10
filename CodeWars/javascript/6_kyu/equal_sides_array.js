// https://www.codewars.com/kata/5679aa472b8f57fb8c000047

function findEvenIndex(arr) {
  for (let i = 0; i < arr.length; i++) {
    if (sumSides(i, arr)) {
      return i;
    }
  }
  return -1;
}

function sumSides(index, arr) {
  let leftSum = 0;
  let rightSum = 0;
  let switchSides = false;
  for (let i = 0; i < arr.length; i++) {
    if (i === index) {
      switchSides = true;
      continue;
    }
    if (switchSides) {
      rightSum += arr[i];
    } else {
      leftSum += arr[i];
    }
  }
  return rightSum === leftSum;
}

// Not part of the solution
function test() {
  const testCases = [
    [1, 2, 3, 4, 3, 2, 1],
    [1, 100, 50, -51, 1, 1],
    [1, 2, 3, 4, 5, 6],
    [20, 10, 30, 10, 10, 15, 35],
    [20, 10, -80, 10, 10, 15, 35],
  ];
  for (let i = 0; i < testCases.length; i++) {
    const nth = i + 1;
    const result = findEvenIndex(testCases[i]);
    console.log(`Test Case #${nth}: ${result}`);
  }
}

test();
