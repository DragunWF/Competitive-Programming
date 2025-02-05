// https://www.codewars.com/kata/583af10620dda4da270000c5/train/javascript

function mergeArrays(a, b) {
  const output = [];
  let cog = true;
  let a_index = 0,
    b_index = 0;
  while (a_index < a.length || b_index < b.length) {
    if (a_index >= a.length) {
      for (let i = b_index; i < b.length; i++) {
        output.push(b[i]);
      }
      break;
    } else if (b_index >= b.length) {
      for (let i = a_index; i < a.length; i++) {
        output.push(a[i]);
      }
      break;
    }
    output.push(cog ? a[a_index++] : b[b_index++]);
    cog = !cog;
  }
  return output;
}

function test() {
  console.log(mergeArrays([1, 2, 3], ["a", "b", "c", "d", "e", "f"]));
}

test();
