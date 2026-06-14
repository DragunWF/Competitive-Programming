// https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/

/**
 * @param {number} n
 * @return {number}
 */
var subtractProductAndSum = function (n) {
  const strNum = String(n);
  let product = parseInt(strNum.charAt(0));
  let sum = 0;
  for (let i = 0; i < strNum.length; i++) {
    const currentNum = parseInt(strNum.charAt(i));
    if (i !== 0) {
      product *= currentNum;
    }
    sum += currentNum;
  }
  return product - sum;
};
