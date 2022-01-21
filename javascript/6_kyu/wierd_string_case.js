// https://www.codewars.com/kata/52b757663a95b11b3d00062d

function toWeirdCase(string) {
  let output = [];
  for (word of string.split(" ")) {
    let index = 0;
    word = word.split("").map((n) => {
      index++;
      return index % 2 >= 1 ? n.toUpperCase() : n;
    });
    output.push(word.join(""));
  }
  return output.join(" ");
}
