// https://www.codewars.com/kata/5783ef69202c0ee4cb000265/train/javascript

function searchArray(array, element) {
  if (!Array.isArray(array) || !Array.isArray(element) || element.length > 2) {
    throw new Error();
  }
  for (let i = 0; i < array.length; i++) {
    if (!Array.isArray(array[i]) || array[i].length > 2) {
      throw new Error();
    }
    if (isEqualArray(array[i], element)) {
      return i;
    }
  }
  return -1;
}

function isEqualArray(array, otherArray) {
  if (array.length !== otherArray.length) {
    return false;
  }
  for (let i = 0; i < array.length; i++) {
    if (array[i] !== otherArray[i]) {
      return false;
    }
  }
  return true;
}

// Not part of the solution
function test() {
  const testCases = [
    [
      [
        [1, 2],
        [3, 4],
        [5, 6],
        [1, 2],
      ],
      [1, 2],
    ],
  ];
  for (let i = 0; i < testCases.length; i++) {
    const result = searchArray(testCases[i][0], testCases[i][1]);
    console.log(`Test Case #${i + 1}: ${result}`);
  }
}

test();
