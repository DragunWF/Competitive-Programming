// https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa

function chooseBestSum(t, k, ls) {
  if (k > ls.length) {
    return null;
  }

  const routes = generateRoutes(k, ls);
  routes.sort((a, b) => a - b);
  for (let distance of routes) {
    if (distance < t) {
      return distance;
    }
  }
}

function generateRoutes(k, ls) {
    
}

function sumDistances(towns) {
  let sum = 0;
  for (let distance of towns) {
    sum += distance;
  }
  return sum;
}
