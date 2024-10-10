// https://www.codewars.com/kata/57f609022f4d534f05000024

function stray(arr) {
  const set = [...new Set(arr)];
  return count(arr, set[0]) > 1 ? set[1] : set[0];
}

function count(arr, element) {
  let count = 0;
  for (let num of arr) {
    if (num === element) {
      count++;
    }
  }
  return count;
}

// Not part of the solution
function test() {
  const testCases = [
    [1, 1, 1, 1, 2, 1],
    [3, 3, 3, 3, 5, 3],
  ];
  for (let i = 0; i < testCases.length; i++) {
    const result = find(testCases[i]);
    console.log(`Test Case ${i + 1}: ${result}`);
  }
}

test();
