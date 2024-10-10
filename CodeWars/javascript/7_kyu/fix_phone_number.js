// https://www.codewars.com/kata/596343a24489a8b2a00000a2/train/javascript

function isItANum(str) {
  const phoneNumber = getPhoneNumber(str);
  if (phoneNumber.length !== 11 || !phoneNumber.startsWith("0")) {
    return "Not a phone number";
  }
  return phoneNumber;
}

function getPhoneNumber(str) {
  const digits = "0123456789";
  let output = "";
  for (let character of str) {
    if (digits.includes(character)) {
      output += character;
    }
  }
  return output;
}

// Not part of the solution
function test() {
  const testCases = [
    "S:)0207ERGQREG88349F82!efRF)",
    "sjfniebienvr12312312312ehfWh",
    "0192387415456",
    "v   uf  f 0tt2eg qe0b 8rtyq4eyq564()(((((165",
    "stop calling me no I have never been in an accident",
  ];
  for (let testCase of testCases) {
    console.log(isItANum(testCase));
  }
}

test();
