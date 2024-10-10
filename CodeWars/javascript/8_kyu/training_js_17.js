// https://www.codewars.com/kata/57277a31e5e51450a4000010/train/javascript

function firstToLast(str, c) {
  let firstPos = null,
    lastPos = null;
  for (let i = 0; i < str.length; i++) {
    if (c === str.charAt(i)) {
      if (firstPos === null) firstPos = i;
      lastPos = i;
    }
  }
  return firstPos === null ? -1 : lastPos - firstPos;
}
