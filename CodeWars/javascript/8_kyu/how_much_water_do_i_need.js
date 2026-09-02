// https://www.codewars.com/kata/575fa9afee048b293e000287/train/javascript

function howMuchWater(water, load, clothes) {
  const maxLoad = load * 2;
  if (clothes > maxLoad) {
    return "Too much clothes";
  }
  if (clothes < load) {
    return "Not enough clothes";
  }
  const waterNeeded = water * 1.1 ** (clothes - load);
  return Math.round(waterNeeded * 100) / 100;
}
