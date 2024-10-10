// https://www.codewars.com/kata/594a2758954a44749f000359

function scratch(lottery) {
  let totalWinValue = 0;
  for (let item of lottery) {
    const piece = item.split(" ");
    const entries = [...piece];
    entries.pop();
    const counts = counter(entries);
    if (possibleWin(counts)) {
      const last = piece[piece.length - 1];
      const winValue = last[0] !== "#" ? Number(last) : 10000;
      totalWinValue += winValue;
    }
  }
  return totalWinValue;
}

function possibleWin(counts) {
  const coatings = counts.hasOwnProperty("coating") ? counts.coating : 0;
  let maxAnimals = 0;
  for (let key in counts) {
    if (key === "coating") continue;
    if (counts[key] === 3) return true; // Early exit
    if (counts[key] > maxAnimals) {
      maxAnimals = counts[key];
    }
  }
  return maxAnimals + coatings >= 3;
}

function counter(arr) {
  const output = {};
  for (let item of arr) {
    if (item[0] === "#") {
      if (!output.hasOwnProperty("coating")) output.coating = 0;
      output.coating++;
    } else if (output.hasOwnProperty(item)) {
      output[item]++;
    } else {
      output[item] = 1;
    }
  }
  return output;
}

// Test code..
console.log(
  scratch([
    "### tiger tiger 100",
    "rabbit dragon ### 10000",
    "### ox ### 1000",
    "### ### ### 10",
    "horse monkey rat ###",
    "dog dog dog ###",
  ])
);
console.log(
  scratch([
    "dragon horse rabbit 10",
    "### ### ### ###",
    "### ### pig 500",
    "dragon pig horse ###",
    "### cock dog 100",
    "snake tiger ### ###",
  ])
);
