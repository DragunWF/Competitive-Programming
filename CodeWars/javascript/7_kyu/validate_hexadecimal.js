// https://www.codewars.com/kata/55a5a70c81e8541d990000bd/train/javascript

function isHex(str) {
  if (str.length !== 6 && str.length !== 3) return false;
  const validChars = "0123456789abcdef".split("");
  for (let char of str.toLowerCase()) {
    if (!validChars.includes(char)) {
      return false;
    }
  }
  return true;
}
