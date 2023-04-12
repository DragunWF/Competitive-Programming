// https://www.codewars.com/kata/5541f58a944b85ce6d00006a

function productFib(prod) {
  let previousNum = 0;
  let currentNum = 1;
  let fibProd = 0;
  while (fibProd < prod && fibProd !== prod) {
    const temp = currentNum;
    currentNum += previousNum;
    previousNum = temp;
    fibProd = currentNum * previousNum;
  }
  return [previousNum, currentNum, fibProd === prod];
}

// Not part of the solution
function test() {
  const testCases = [714, 800];
  for (let i = 0; i < testCases.length; i++) {
    const result = productFib(testCases[i]);
    console.log(`Test Case #${i + 1}: ${result}`);
  }
}

test();
