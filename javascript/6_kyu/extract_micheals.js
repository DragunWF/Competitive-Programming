// https://www.codewars.com/kata/580741302e14acaef900015a

function getMichaelLastName(text) {
  const symbols = ["!", "?", ".", ","];
  let names = [];
  text = text.split(" ");
  for (let i = 1; i < text.length; i++) {
    if (text[i][0] === text[i][0].toUpperCase()) {
      if (text[i - 1].includes("Michael")) {
        for (let x of symbols) {
          while (text[i].includes(x)) text[i] = text[i].replace(x, "");
        }
        names.push(text[i]);
      }
    }
  }
  return names;
}
