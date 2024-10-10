// https://www.codewars.com/kata/511f11d355fe575d2c000001/train/javascript

function twoOldestAges(ages) {
  ages.sort((a, b) => b - a);
  return [ages[1], ages[0]];
}
