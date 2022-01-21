// https://www.codewars.com/kata/5547929140907378f9000039

function shortcut(string) {
  let vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"];
  return string
    .split("")
    .filter((n) => {
      return !vowels.includes(n) ? n : "";
    })
    .join("");
}
