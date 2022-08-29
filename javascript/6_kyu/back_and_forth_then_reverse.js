// https://www.codewars.com/kata/60cc93db4ab0ae0026761232/train/javascript

function arrange(s) {
  const t = [];
  let reverse = false;
  for (let i = 0; i < Math.ceil(s.length / 2); i++) {
    const lastIndex = s.length - (1 + i);
    if (!reverse) {
      t.push(s[i]);
      if (lastIndex != i) t.push(s[lastIndex]);
    } else {
      if (lastIndex != i) t.push(s[lastIndex]);
      t.push(s[i]);
    }
    reverse = reverse ? false : true;
  }
  return t;
}

console.log(arrange([1, 2])); // [1, 2]
console.log(arrange([4, 3, 2])); // [4, 2, 3]
console.log(arrange([2, 4, 3, 4])); // [2, 4, 3, 4]
console.log(arrange([9, 7, -2, 8, 5, -3, 6, 5, 1])); // [9, 1, 5, 7, -2, 6, -3, 8, 5]
