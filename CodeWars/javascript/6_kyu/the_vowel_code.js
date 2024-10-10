// https://www.codewars.com/kata/53697be005f803751e0015aa/train/javascript

function encode(string) {
  return perform(string, true);
}

function decode(string) {
  return perform(string);
}

function perform(string, isEncode = false) {
  const vowels = "aeiou",
    nums = "12345";
  let output = "";
  for (let char of string) {
    if (isEncode && vowels.includes(char)) {
      output += vowels.indexOf(char) + 1;
      continue;
    } else if (!isEncode && nums.includes(char)) {
      output += vowels[Number(char) - 1];
      continue;
    }
    output += char;
  }
  return output;
}
