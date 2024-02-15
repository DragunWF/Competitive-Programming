// https://www.codewars.com/kata/563cf89eb4747c5fb100001b/train/javascript

function removeSmallest(numbers) {
  let index = 0,
    minValue = numbers[0];
  const output = [...numbers];
  for (let i = 1; i < numbers.length; i++) {
    if (numbers[i] < minValue) {
      index = i;
      minValue = numbers[i];
    }
  }
  output.splice(index, 1);
  return output;
}
