// https://www.codewars.com/kata/54ba84be607a92aa900000f1

function isIsogram(str) {
  str = str.toLowerCase();
  if ([...new Set(str.split(""))].length === str.length) {
    return false;
  }
  for (let i = 0; i < str.length - 1; i++) {
    if (str[i] === str[i + 1]) {
      return false;
    }
  }
  return true;
}

// Not part of the solution
function test() {
  const testCases = ["isogram", "moOse", "aba", "Dermatoglyphics"];
  for (let i = 0; i < testCases.length; i++) {
    const result = isIsogram(testCases[i]);
    console.log(`Test Case #${i + 1}: ${result}`);
  }
}

test();
