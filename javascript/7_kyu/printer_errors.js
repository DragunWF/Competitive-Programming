// https://www.codewars.com/kata/56541980fa08ab47a0000040

function printerError(s) {
  const colors = "abcdefghijklm".split("");
  let x = 0;
  for (c of s) {
    if (!colors.includes(c)) x++;
  }
  return `${x}/${s.length}`;
}
