// https://www.codewars.com/kata/529eef7a9194e0cbc1000255

var isAnagram = function (test, org) {
  test = test.toLowerCase().split("");
  org = org.toLowerCase().split("");
  for (c of test.length > org.length ? test : org) {
    if (test.length < org.length ? test : org.includes(c)) {
      if (count(test, c) !== count(org, c)) return false;
    } else return false;
  }
  return true;
};

function count(array, element) {
  let count = 0;
  for (e of array) {
    if (e === element) count++;
  }
  return count;
}
