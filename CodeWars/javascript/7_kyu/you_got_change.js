// https://www.codewars.com/kata/5966f6343c0702d1dc00004c/train/javascript

function giveChange(amount) {
  let currentAmount = amount;
  const sequence = [1, 5, 10, 20, 50, 100];
  const changeCount = [0, 0, 0, 0, 0, 0];
  for (let i = sequence.length - 1; i >= 0; i--) {
    const change = Math.trunc(currentAmount / sequence[i]);
    changeCount[i] = change;
    currentAmount -= change * sequence[i];
  }
  return changeCount;
}
