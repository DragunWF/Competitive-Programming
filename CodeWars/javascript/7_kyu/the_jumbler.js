// https://www.codewars.com/kata/69269262ced9e95dc63abd1e

function jumbler(indices) {
  let jumbleCount = 0;
  let currentValue = indices[0];
  while (currentValue != 0) {
    for (let i = 0; i < indices.length; i++) {
      if (i === currentValue) {
        const targetValue = indices[i];
        const newIndices = [];
        for (let j = 0; j < indices.length; j++) {
          if (i !== j) {
            newIndices.push(indices[j]);
          }
        }
        indices = [targetValue, ...newIndices];
      }
    }
    currentValue = indices[0];
    jumbleCount++;
  }
  return jumbleCount;
}
