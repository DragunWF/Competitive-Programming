// https://www.codewars.com/kata/69b9359e8af0beedadc87db9

function identifyMonster(observedWeaknesses, bestiary) {
  for (let monster of Object.keys(bestiary)) {
    let includesAll = true;
    for (let weakness of observedWeaknesses) {
      if (!bestiary[monster].includes(weakness)) {
        includesAll = false;
        break;
      }
    }
    if (includesAll) {
      return monster;
    }
  }
  return "Unknown monster";
}

function test() {
  const bestiary = {
    Griffin: ["Grapeshot", "Hybrid Oil", "Aard"],
    Noonwraith: ["Yrden", "Moon Dust", "Specter Oil"],
    Drowner: ["Igni", "Necrophage Oil"],
  };

  // Expected - Returns: "Drowner"
  console.log(identifyMonster(["Igni", "Necrophage Oil"], bestiary));

  // Expected - Returns: "Noonwraith" (since these vulnerabilities are in its list)
  console.log(identifyMonster(["Yrden", "Moon Dust"], bestiary));

  // Expected - Returns: "Unknown monster"
  console.log(identifyMonster(["Silver", "Garlic"], bestiary));
}
