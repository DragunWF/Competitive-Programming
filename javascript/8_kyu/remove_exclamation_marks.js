// https://www.codewars.com/kata/57faf12b21c84b5ba30001b0/train/javascript

function remove(string) {
  let output = "";
  for (let i = 0; i < string.length; i++) {
    if (string[i] !== "!") {
      output += string[i];
    }
  }
  return output + "!";
}
