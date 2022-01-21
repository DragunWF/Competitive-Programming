// https://www.codewars.com/kata/52c31f8e6605bcc646000082

function twoSum(arr, tg) {
  const values = [];
  let cog = false;
  for (let n = 0; n < arr.length; n++) {
    for (let e = arr.length - 1; e >= 0; e--) {
      if (arr[n] + arr[e] === tg) {
        values.push(n, e), (cog = true);
        break;
      }
    }
    if (cog) break;
  }
  return values;
}
