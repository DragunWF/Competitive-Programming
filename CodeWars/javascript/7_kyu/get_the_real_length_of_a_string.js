// https://www.codewars.com/kata/599c4b69eb8e49effa000079/train/javascript

function getRealLength(string) {
  let realLength = 0;
  for (let char of string) realLength++;
  return realLength;
}

function test() {
  console.log(getRealLength("𝓪𝓫𝓬𝓭"));
  console.log(getRealLength("😸🦌🚀"));
}

test();
