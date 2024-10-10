// https://www.codewars.com/kata/57fae964d80daa229d000126/train/javascript

function remove(string) {
  return string[string.length - 1] === "!"
    ? string.substring(0, string.length - 1)
    : string;
}
