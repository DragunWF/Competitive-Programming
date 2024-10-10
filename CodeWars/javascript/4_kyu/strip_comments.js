// https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/javascript

function solution(input, markers) {
  const array = input.split(" ");
  let output = [];
  let removeNext = false;
  for (let item of array) {
    let marker = false;
    for (let chr of item) {
      if (markers.includes(chr)) {
        marker = true;
        if (item.length <= 1) removeNext = true;
      }
    }
    if (!marker && !removeNext) output.push(item);
    if (removeNext) removeNext = false;
  }
  return output.join(" ");
}

console.log(
  solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
);
