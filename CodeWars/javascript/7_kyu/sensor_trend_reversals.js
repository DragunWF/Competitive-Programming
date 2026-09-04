// https://www.codewars.com/kata/6a6bdaca77f722e42da8fba6/train/javascript

function countDirectionChanges(readings) {
  if (!readings.length) {
    return 0;
  }
  let count = 0;
  let isIncreasing = readings[1] >= readings[0];
  for (let i = 2; i < readings.length; i++) {
    if (readings[i] === readings[i - 1]) {
      continue;
    }
    if (readings[i] > readings[i - 1]) {
      if (!isIncreasing) {
        count++;
      }
      isIncreasing = true;
    } else {
      if (isIncreasing) {
        count++;
      }
      isIncreasing = false;
    }
  }
  return count;
}
