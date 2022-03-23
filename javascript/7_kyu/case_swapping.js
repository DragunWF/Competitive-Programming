// https://www.codewars.com/kata/5590961e6620c0825000008f/train/python

function swap(str) {
  return str.split("").map((c) => {
    return c == c.toLowerCase() ? c.toUpperCase() : c.toLowerCase();
  }).join("");
}
