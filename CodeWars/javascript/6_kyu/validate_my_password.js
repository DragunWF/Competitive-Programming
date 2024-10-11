// https://www.codewars.com/kata/59c01248bf10a47bd1000046/train/javascript

function validPass(password) {
  if (!(password.length > 3 && password.length < 20)) return "INVALID";
  const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
  const digits = "0123456789";
  let hasDigit = false,
    hasLetter = false;
  for (let char of password) {
    if (!letters.includes(char) && !digits.includes(char)) return "INVALID";
    if (letters.includes(char)) hasLetter = true;
    else if (digits.includes(char)) hasDigit = true;
  }
  return hasLetter && hasDigit ? "VALID" : "INVALID";
}
