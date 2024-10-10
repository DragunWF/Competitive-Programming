// https://www.codewars.com/kata/53b138b3b987275b46000115

function compareVersions(v1, v2) {
  v1 = v1.split(".").map((n) => {
    return Number(n);
  });
  v2 = v2.split(".").map((n) => {
    return Number(n);
  });
  for (let i = 0; i < v1.length; i++) {
    if (v1[i] > v2[i]) return true;
    else if (v1[i] < v2[i]) return false;
    if (i === v1.length - 1) {
      if (v1[i] === v2[i] && v1.length >= v2.length) return true;
      else if (v1.length > v2.length) return true;
      else return false;
    }
  }
}
