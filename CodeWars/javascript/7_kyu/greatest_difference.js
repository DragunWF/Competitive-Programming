// https://www.codewars.com/kata/56b12e3ad2387de332000041/train/javascript

function diff(strList) {
  let greatestDiff = 0;
  let selectedCouple = null;
  for (let item of strList) {
    const values = item.split("-");
    const diff = Math.abs(Number(values[0]) - Number(values[1]));
    if (diff !== 0 && diff > greatestDiff) {
      greatestDiff = diff;
      selectedCouple = item;
    }
  }
  return !selectedCouple ? false : selectedCouple;
}
