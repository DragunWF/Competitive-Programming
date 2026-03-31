// https://www.codewars.com/kata/5732b0351eb838d03300101d/train/javascript

function blackAndWhite(arr) {
  if (!Array.isArray(arr)) return "It's a fake array";
  const fiveIsPresent = arr.indexOf(5) !== -1;
  const thirteenIsPresent = arr.indexOf(13) !== -1;
  if (fiveIsPresent && thirteenIsPresent) return "It's a black array";
  return "It's a white array";
}
