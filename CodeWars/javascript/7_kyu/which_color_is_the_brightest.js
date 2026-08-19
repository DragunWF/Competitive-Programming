// https://www.codewars.com/kata/62eb800ba29959001c07dfee/train/javascript

function brightest(colors) {
  let brightestHexadecimal = null;
  let maxValue = -1;
  for (let color of colors) {
    const r = parseInt(color.slice(1, 3), 16);
    const g = parseInt(color.slice(3, 5), 16);
    const b = parseInt(color.slice(5, 7), 16);

    const value = Math.max(r, g, b);
    if (value > maxValue) {
      maxValue = value;
      brightestHexadecimal = color;
    }
  }
  return brightestHexadecimal;
}
