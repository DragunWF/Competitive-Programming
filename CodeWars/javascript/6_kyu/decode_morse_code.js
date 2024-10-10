// https://www.codewars.com/kata/54b724efac3d5402db00065e

function decodeMorse(morseCode) {
  let output = "";
  let recentSpace = false;
  for (let code of morseCode.trim().split(" ")) {
    if (MORSE_CODE[code]) {
      output += MORSE_CODE[code];
      recentSpace = false;
    } else if (!recentSpace) {
      output += " ";
      recentSpace = true;
    }
  }
  return output;
}
