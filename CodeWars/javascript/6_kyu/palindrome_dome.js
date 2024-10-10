// https://www.codewars.com/kata/53046ceefe87e4905e00072a/train/javascript

function palindrome(string) {
  const validChars = "abcdefghijklmnopqrstuvwxyz0123456789";
  const raw = string.split("").filter((n) => {
    return validChars.includes(n.toLowerCase());
  });
  const original = convert(raw);
  raw.reverse();
  return original === convert(raw);
}

function convert(arr) {
  return arr.join("").toLowerCase();
}

// Not part of the solution
function test() {
  const testCases = [
    "Amore, Roma",
    "A man, a plan, a canal: Panama",
    "No 'x' in 'Nixon'",
    "Abba Zabba, you're my only friend",
  ];
  for (let testCase of testCases) {
    console.log(palindrome(testCase));
  }
}

test();
