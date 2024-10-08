// https://www.codewars.com/kata/515dfd2f1db09667a0000003/train/javascript

function keysAndValues(data) {
  const output = [[], []];
  for (let key in data) {
    output[0].push(key);
    output[1].push(data[key]);
  }
  return output;
}
