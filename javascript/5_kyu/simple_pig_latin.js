// https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/javascript

function pigIt(str) {
  const punctuations = ["!", "?", ".", ";", ":", ","];
  return str
    .split(" ")
    .map((w) => {
      if (punctuations.includes(w)) return w;
      return w.concat(`${w[0]}ay`).substring(1);
    })
    .join(" ");
}

console.log(pigIt("Pig latin is cool !"));
