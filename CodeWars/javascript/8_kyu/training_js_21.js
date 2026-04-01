// https://www.codewars.com/kata/5729b103dd8bac11a900119e/train/javascript

function fiveLine(s) {
  s = s.trim();
  const lines = [];
  for (let i = 1; i <= 5; i++) {
    let line = "";
    for (let j = 0; j < i; j++) {
      line += s;
    }
    lines.push(line);
  }
  return lines.join("\n");
}
