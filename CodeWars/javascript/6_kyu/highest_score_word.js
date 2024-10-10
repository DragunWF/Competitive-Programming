// https://www.codewars.com/kata/57eb8fcdf670e99d9b000272

function high(x) {
  let alp = "abcdefghijklmnopqrstuvwxyz".split("");
  let output = "";
  let total = 0;
  for (word of x.split(" ")) {
    let score = 0;
    for (ltr of word) {
      if (alp.includes(ltr)) score += alp.indexOf(ltr) + 1;
    }
    console.log(score, word);
    if (score > total) {
      output = word;
      total = score;
    }
  }
  return output;
}
