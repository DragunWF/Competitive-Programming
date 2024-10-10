// https://www.codewars.com/kata/52ad1db4b2651f744d000394

function reindeers(presents) {
  if (presents > 180) throw new Error();
  return Math.ceil(presents / 30) + 2;
}
