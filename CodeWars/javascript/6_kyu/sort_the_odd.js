// https://www.codewars.com/kata/578aa45ee9fd15ff4600090d

function sortArray(array) {
  for (let i = 0; i < array.length; i++) {
    let oddIndex = null;
    for (let j = 0; j < array.length; j++) {
      const isOdd = array[j] % 2 !== 0;
      if (isOdd) {
        if (oddIndex !== null && array[j] < array[oddIndex]) {
          const temp = array[j];
          array[j] = array[oddIndex];
          array[oddIndex] = temp;
        }
        oddIndex = j;
      }
    }
  }
  return array;
}

// Not part of the solution
function test() {
  const testCases = [[5, 3, 2, 8, 1, 4], [5, 3, 1, 8, 0], []];
  for (let i = 0; i < testCases.length; i++) {
    const nth = i + 1;
    const result = sortArray(testCases[i]);
    console.log(`Test Case #${nth}: [${result}]`);
  }
}

test();
