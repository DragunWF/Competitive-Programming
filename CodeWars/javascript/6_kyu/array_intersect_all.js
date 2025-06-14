// https://www.codewars.com/kata/52a4e42ce950ed50da000748/train/javascript

function intersect(...arrays) {
  const counter = {};
  for (let array of arrays) {
    for (let item of array) {
      if (item in counter) {
        counter[item]++;
      } else {
        counter[item] = 1;
      }
    }
  }

  const output = [];
  for (let key of Object.keys(counter)) {
    if (counter[key] === arrays.length) {
      output.push(key);
    }
  }
  return output;
}
