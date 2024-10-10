// https://www.codewars.com/kata/5720a1cb65a504fdff0003e2

function differenceInAges(ages) {
  const min = Math.min(...ages),
    max = Math.max(...ages);
  return [min, max, max - min];
}
