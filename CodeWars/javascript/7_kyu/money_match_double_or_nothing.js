// https://www.codewars.com/kata/5d378318e04cd7001ad72a27/train/javascript

function doubleOrNothing(cash, wager, losses) {
  let totalCost = wager;
  for (let i = 0; i < losses - 1; i++) {
    totalCost *= 2;
  }
  let remainingCash = cash - totalCost;
  return remainingCash < 0 ? "I'll pay you back later" : remainingCash;
}
