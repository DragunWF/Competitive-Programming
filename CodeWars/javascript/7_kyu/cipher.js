// https://www.codewars.com/kata/5a19701d80171fd71d000029/train/javascript

function encode(str) {
  const cipherCharacters = [];
  for (let i = 0; i < str.length; i++) {
    cipherCharacters.push(String.fromCharCode(str.charCodeAt(i) * 6));
  }
  return cipherCharacters.join("");
}

function decode(str) {
  const plainCharacters = [];
  for (let i = 0; i < str.length; i++) {
    plainCharacters.push(String.fromCharCode(str.charCodeAt(i) / 6));
  }
  return plainCharacters.join("");
}

function test() {
  const input = "Hello World!";
  const ciphertext = encode(input);
  console.log(`Ciphertext: ${ciphertext}`);
  console.log(`Plaintext: ${decode(ciphertext)}`);
}

test();
