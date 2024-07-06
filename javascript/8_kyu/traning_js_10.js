// https://www.codewars.com/kata/5721a78c283129e416000999/train/javascript

function pickIt(arr) {
  let output = [[], []];
  for (let num of arr) {
    output[(num + 1) % 2].push(num);
  }
  return output;
}
