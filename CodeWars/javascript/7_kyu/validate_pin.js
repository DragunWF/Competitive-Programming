// https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/javascript

function validatePIN(pin) {
  const digits = "0123456789";
  for (let character of pin) {
    if (!digits.includes(character)) {
      return false;
    }
  }
  return pin.length === 4 || pin.length === 6;
}

// Not part of the solution
function test() {
  const testCases = ["1234", "12345", "a234"];
  for (let i = 0; i < testCases.length; i++) {
    const result = validatePIN(testCases[i]);
    console.log(`Test Case #${i + 1}: ${result}`);
  }
}

test();
