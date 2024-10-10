// https://www.codewars.com/kata/562e6df5cf2d3908ad00019e/train/javascript

function separateLiquids(liquid) {
  if (!liquid.length) {
    return [];
  }
  const density = { H: 1.36, W: 1.0, A: 0.87, O: 0.8 };
  const combined = combineArr(liquid);
  for (let i = 0; i < combined.length; i++) {
    for (let j = 0; j < combined.length - 1; j++) {
      if (density[combined[j]] > density[combined[j + 1]]) {
        const temp = combined[j];
        combined[j] = combined[j + 1];
        combined[j + 1] = temp;
      }
    }
  }
  return reformArr(combined, liquid[0].length);
}

function combineArr(liquid) {
  const output = [];
  for (let element of liquid) {
    output.push(...element);
  }
  return output;
}

function reformArr(combined, n) {
  const output = [];
  let block = [];
  for (let i = 0; i < combined.length; i++) {
    const nth = i + 1;
    block.push(combined[i]);
    if (nth % n === 0) {
      output.push(block);
      block = [];
    }
  }
  return output;
}

// Not part of the solution
function test() {
  const testCases = [
    [
      ["H", "H", "W", "O"],
      ["W", "W", "O", "W"],
      ["H", "H", "O", "O"],
    ],
  ];
  for (let i = 0; i < testCases.length; i++) {
    const result = separateLiquids(testCases[i]);
    console.log(`Test Case #${i + 1}: ${result}`);
  }
}

test();
