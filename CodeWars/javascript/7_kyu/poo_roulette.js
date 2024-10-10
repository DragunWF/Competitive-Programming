// https://www.codewars.com/kata/5bc9bc4e703b2d2081000001/train/javascript

function pooRoulette(p) {
  for (let i = 0; i < p.length; i++) {
    for (let j = 0; j < p[i].length; j++) {
      if (p[i][j] === "~" || p[i][j] === "B") {
        if (
          i + 3 < p.length &&
          p[i + 1][j] === "~" &&
          p[i + 2][j] === "~" &&
          (p[i + 3][j] === "B" || p[i + 3][j] === "~")
        ) {
          return "Get the wipes!";
        }
        if (
          j + 3 < p[i].length &&
          p[i][j + 1] === "~" &&
          p[i][j + 2] === "~" &&
          (p[i][j + 3] === "B" || p[i][j + 3] === "~")
        ) {
          return "You disgust me!";
        }
      }
    }
  }
  return "Calm before the storm";
}
