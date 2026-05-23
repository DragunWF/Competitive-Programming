// https://www.codewars.com/kata/595877be60d17855980013d3/train/javascript

function euclideanDistance(point1, point2) {
  let total = 0;
  for (let i = 0; i < point1.length; i++) {
    total += (point2[i] - point1[i]) ** 2;
  }
  return Math.sqrt(total);
}
