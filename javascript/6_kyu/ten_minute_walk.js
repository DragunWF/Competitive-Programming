// https://www.codewars.com/kata/54da539698b8a2ad76000228

function isValidWalk(walk) {
  if (walk.length !== 10) return false;
  const x_axis = ["w", "e"];
  let x = 0;
  let y = 0;
  for (d of walk) {
    if (x_axis.includes(d)) x += d === "e" ? 1 : -1;
    else y += d === "n" ? 1 : -1;
  }
  return x === 0 && y === 0;
}
