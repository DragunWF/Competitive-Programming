// https://www.codewars.com/kata/5526fc09a1bbd946250002dc

function findOutlier(int) {
  let even = 0;
  let odd = 0;
  for (n of int) {
    if (even > 1 || odd > 1) break;
    if (!(n % 2)) even++;
    else odd++;
  }
  return Number(
    int.filter((e) => {
      if (even > odd && e % 2 !== 0) return e;
      if (even < odd && e % 2 === 0) return e;
    })
  );
}
