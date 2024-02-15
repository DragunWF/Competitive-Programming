// https://www.codewars.com/kata/5bb904724c47249b10000131/train/javascript

function points(games) {
  let total = 0;
  for (let score of games) {
    const [x, y] = score.split(":").map((x) => Number(x));
    if (x === y) total++;
    else if (x > y) total += 3;
  }
  return total;
}
