// https://www.codewars.com/kata/570bcd9715944a2c8e000009/train/javascript

function sc(floor) {
  if (floor <= 1) return "";
  const screams = [];
  for (let i = 0; i < floor - 1; i++) {
    screams.push("Aa~");
  }
  screams.push("Pa!");
  if (floor <= 6) screams.push("Aa!");
  return screams.join(" ");
}
