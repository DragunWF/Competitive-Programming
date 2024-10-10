// https://www.codewars.com/kata/59df2f8f08c6cec835000012

function meeting(s) {
  const m = [];
  for (x of s.split(";")) {
    const y = x.split(":");
    m.push(`(${y[1].toUpperCase()}, ${y[0].toUpperCase()})`);
  }
  return m.sort().join("");
}
