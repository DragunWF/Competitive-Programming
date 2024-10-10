// https://www.codewars.com/kata/5a651865fd56cb55760000e0/train

function arrayLeaders(numbers) {
  const leaders = [];
  let sum = 0;
  for (let i = numbers.length - 1; i >= 0; i--) {
    if (numbers[i] > sum) {
      leaders.push(numbers[i]);
    }
    sum += numbers[i];
  }
  leaders.reverse();
  return leaders;
}
