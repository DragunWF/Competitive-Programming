// https://www.codewars.com/kata/59dc8288fc3c49cc3f000039/train/javascript

function sort(initialArray, sortingArray) {
  const output = [];
  for (let i = 0; i < initialArray.length; i++) output.push(null);
  for (let i = 0; i < initialArray.length; i++) {
    output[sortingArray[i]] = initialArray[i];
  }
  return output;
}
