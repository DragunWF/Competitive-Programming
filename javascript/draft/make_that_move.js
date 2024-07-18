// https://www.codewars.com/kata/6611b3ccb42a1927e9663bf7/train/javascript

function move(s) {
  const directionChangeTiles = [];
  let index = 0;
  let currentTile;
  let moveRight = true;
  while (index >= 0 && index < s.length) {
    currentTile = s[index];
    if (currentTile === "o") return currentTile;
    else if (currentTile === "p" || currentTile === "q") {
      moveRight = currentTile === "p";
      directionChangeTiles.push(currentTile);
      if ([...new Set(directionChangeTiles)].length >= 2) return "x";
    }
    moveRight ? index++ : index--;
  }
  return index < s.length ? "q" : "p";
}

function test() {
  // Not part of the solution, just testing
  const exampleTestCases = [
    [".....", "p"],
    ["..o..", "o"],
    ["p....", "p"],
    ["q....", "q"],
    ["....p", "p"],
    ["....q", "q"],
    ["p..o.", "p"],
    ["....p............p....", "p"],
    ["....p............p..q.", "q"],
    ["....p......q.....p..q.", "x"],
    ["....p...o..q.....p..q.", "o"],
    [".q..p............p..q.", "q"],
  ];
  for (let testCase of exampleTestCases) {
    const result = move(testCase[0]);
    console.log(`${testCase[0]} === ${result}, ${testCase[1] === result}`);
  }
}

test();
