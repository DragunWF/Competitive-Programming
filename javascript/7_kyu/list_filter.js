// https://www.codewars.com/kata/53dbd5315a3c69eed20002dd

function filter_list(arr) {
  return arr.filter((x) => {
    if (typeof x !== "string") return x || x === 0;
  });
}
