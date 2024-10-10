// https://www.codewars.com/kata/57a0885cbb9944e24c00008e

function removeExclamationMarks(s) {
  while (s.includes("!")) s = s.replace("!", "");
  return s;
}
