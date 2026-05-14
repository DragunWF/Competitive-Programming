// https://www.codewars.com/kata/5a84d485742ba347b90006b7/train/javascript

function howManyGifts(maxBudget, gifts) {
  gifts.sort((a, b) => a - b);
  let totalCost = 0;
  let giftCount = 0;
  for (let gift of gifts) {
    if (totalCost + gift <= maxBudget) {
      totalCost += gift;
      giftCount++;
    }
  }
  return giftCount;
}
