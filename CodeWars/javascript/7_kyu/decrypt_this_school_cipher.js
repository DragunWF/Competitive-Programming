// https://www.codewars.com/kata/5cd48cffaae6e30018943175

const decrypt = (str) => {
  let isOpen = false;
  const output = [];
  let currentCharCode = [];
  for (let char of str) {
    if (char === "'") {
      if (isOpen) {
        isOpen = false;
        const convertedCharCode = Number(currentCharCode.join(""));
        output.push(String.fromCharCode(convertedCharCode));
        currentCharCode = [];
        continue;
      }
      isOpen = true;
    } else {
      if (isOpen) {
        currentCharCode.push(char);
        continue;
      }
      output.push(char);
    }
  }
  output.reverse();
  return output.join("");
};
