// https://www.codewars.com/kata/570cc83df616a85944001315

function countWords(str) {
  while (str.includes("﻿")) str = str.replace("﻿", " ");
  return str.split(" ").filter((ch) => {
    if (ch) return ch;
  }).length;
}
