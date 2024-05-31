// https://www.codewars.com/kata/545a4c5a61aa4c6916000755/train/javascript

function gimme(triplet) {
  const max = Math.max(triplet),
    min = Math.min(triplet);
  for (let i = 0; i < triplet.length; i++) {
    if (triplet[i] !== max && triplet[i] !== min) {
      return i;
    }
  }
}
