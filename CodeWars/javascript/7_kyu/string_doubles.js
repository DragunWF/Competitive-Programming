// https://www.codewars.com/kata/5a145ab08ba9148dd6000094/train/javascript

function doubles(s) {
  let output = "";
  let isPairPresent;

  do {
    isPairPresent = false;
    for (let i = 0; i < s.length; i++) {
      if (i < s.length - 1 && s[i] === s[i + 1]) {
        i++;
        isPairPresent = true;
        continue;
      }
      output += s[i];
    }
    s = output;
    output = "";
  } while (isPairPresent);

  return s;
}

function test() {
  console.log(doubles("abbbzz")); // ab
  console.log(doubles("aabbcc")); // ""
  console.log(doubles("aaaabbbbz"));
  console.log(doubles("abba")); // ""
}

test();
