// https://www.codewars.com/kata/56971747aa359bdbf800004d/train/javascript

function trickyDoubles(n) {
  const strNum = n.toString();
  if (strNum.length % 2 === 0) {
    const firstHalf = strNum.substring(0, strNum.length / 2);
    const secondHalf = strNum.substring(strNum.length / 2);
    return firstHalf === secondHalf ? Number(strNum) : n * 2;
  }
  return n * 2;
}

// Not part of the solution but is used for testing
function test() {
  console.log(trickyDoubles(4343)); // 4343
  console.log(trickyDoubles(55)); // 55
  console.log(trickyDoubles(5000)); // 10000
}

test();
