// https://www.codewars.com/kata/6912508732aab96c59c09c7d/train/javascript

function reloadSheeps(arr) {
  const output = [];
  const allChars = "eehps";
  for (let sheep of arr) {
    const chars = sheep.split("");
    chars.sort();
    if (allChars === chars.join("")) {
      output.push("sheep");
    }
  }
  return output;
}
