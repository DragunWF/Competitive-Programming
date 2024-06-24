// https://www.codewars.com/kata/5868812b15f0057e05000001/train/javascript

function tailSwap(arr) {
  const a = arr[0].split(":"),
    b = arr[1].split(":");
  return [`${a[0]}:${b[1]}`, `${b[0]}:${a[1]}`];
}
