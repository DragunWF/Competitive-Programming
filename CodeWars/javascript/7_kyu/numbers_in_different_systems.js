// https://www.codewars.com/kata/588bb1195eb601f5d400001f/train/javascript

function sysNums(n, sys) {
  if (n === 0 && sys === 16) return +0;
  const strNum = n.toString(sys);
  return isAllDigits(strNum) ? Number(strNum) : strNum;
}

function isAllDigits(n) {
  const digits = "0123456789";
  for (let char of n) {
    if (!digits.includes(char)) {
      return false;
    }
  }
  return true;
}
