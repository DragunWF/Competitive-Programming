// https://www.codewars.com/kata/5884d46015a70f6cd7000035/train/javascript

function inter(s1, s2) {
  const output = new Set();
  for (let item of s1) {
    if (s2.has(item)) {
      output.add(item);
    }
  }
  return output;
}
