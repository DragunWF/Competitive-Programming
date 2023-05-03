// https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/javascript

function deleteNth(arr, n) {
  const existing = [],
    output = [],
    elements = [];
  for (let item of arr) {
    if (!existing.includes(item)) {
      existing.push(item);
      elements.push({ num: item, occurences: 1 });
      output.push(item);
    } else if (checkOccurences(elements, item, n)) {
      output.push(item);
    }
  }
  return output;
}

function checkOccurences(elements, item, n) {
  for (let i = 0; i < elements.length; i++) {
    if (elements[i].num === item) {
      elements[i].occurences++;
      return elements[i].occurences <= n;
    }
  }
}

// Not part of the solution
function test() {
  const testCases = [
    [[20, 37, 20, 21], 1],
    [[1, 1, 3, 3, 7, 2, 2, 2, 2], 3],
  ];
  for (let i = 0; i < testCases.length; i++) {
    const result = deleteNth(testCases[i][0], testCases[i][1]);
    console.log(`Test Case #${i + 1}: ${result}`);
  }
}

test();
