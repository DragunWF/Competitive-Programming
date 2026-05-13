// https://www.codewars.com/kata/594a7ea087a7c6cbe60000d6/train/javascript

f = (_) => "\x48\x65\x6c\x6c\x6f\x2c\x20\x77\x6f\x72\x6c\x64\x21";

f_old = (_) => {
  const codes = [72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33];
  let output = "";
  const func = "f\x72omCodePoint";
  for (let code of codes) {
    output += String[func](code);
  }
  return output;
};
