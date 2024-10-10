// https://www.codewars.com/kata/5298ad7cd0f550269500051b/train/javascript

function zipObject(keys, values) {
  const output = {};
  if (values) {
    for (let i = 0; i < keys.length; i++) {
      output[keys[i]] = values ? values[i] : undefined;
    }
  } else {
    const newKeys = searchPair(keys);
    for (let i = 0; i < newKeys.length; i++) {
      output[newKeys[i][0]] =
        newKeys[i].length === 1 ? undefined : newKeys[i][1];
    }
  }
  return output;
}

function searchPair(arr) {
  if (!arr.length) return [];
  return Array.isArray(arr[0][0]) ? searchPair(arr[0]) : arr;
}

// Not part of the solution
function test() {
  const testCases = [
    [
      [
        [
          ["a", 1],
          ["b", 2],
        ],
      ],
      undefined,
    ],
    [[[["a"], ["b"]]], undefined],
  ];
  for (let testCase of testCases) {
    console.log(zipObject(testCase[0], testCase[1]));
  }
}

test();
