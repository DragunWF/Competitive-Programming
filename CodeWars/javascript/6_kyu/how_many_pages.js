// https://www.codewars.com/kata/622de76d28bf330057cd6af8/train/python

function amountOfPages(summary) {
  let output = "";
  for (let i = 1; i < summary + 1; i++) {
    output += i.toString();
    if (output.length >= summary) return i;
  }
}
