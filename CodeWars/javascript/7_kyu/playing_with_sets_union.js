// https://www.codewars.com/kata/5884ce61f36b6d738b000053/train/javascript

function union(s1, s2) {
  const unionSet = [];
  for (let num of s1) {
    unionSet.push(num);
  }
  for (let num of s2) {
    unionSet.push(num);
  }
  return new Set([...unionSet]);
}
