// https://www.codewars.com/kata/550498447451fbbd7600041c/train/javascript

function comp(array1, array2) {
  try {
    array1 = array1
      .map((n) => { return n * n; })
      .sort((a, b) => { return a - b; });
    array2.sort((a, b) => { return a - b; });
    for (let i = 0; i < array1.length; i++)
      if (array1[i] !== array2[i]) return false;
    return true;
  } catch (error) {
    return false;
  }
}

a1 = [121, 144, 19, 161, 19, 144, 19, 11];
a2 = [
  11 * 11,
  121 * 121,
  144 * 144,
  19 * 19,
  161 * 161,
  19 * 19,
  144 * 144,
  19 * 19,
];
console.log(comp(a1, a2));
