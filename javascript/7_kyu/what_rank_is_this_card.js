// https://www.codewars.com/kata/59cbcb4523dacc2ccd000030/solutions/javascript

function rank(card) {
  if (card[0] === "1") return 0;
  const values = { T: 10, J: 11, Q: 12, K: 13, A: 14 };
  if (Object.keys(values).includes(card[0])) return values[card[0]];
  return Number(card[0]) ? Number(card[0]) : 0;
}
