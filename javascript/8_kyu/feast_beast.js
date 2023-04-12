// https://www.codewars.com/kata/5aa736a455f906981800360d/train/javascript

function feast(beast, dish) {
  return (
    beast.startsWith(dish.charAt(0)) &&
    beast.endsWith(dish.charAt(dish.length - 1))
  );
}

// Not part of the solution
function test() {
  const testCases = [
    ["great blue heron", "garlic naan"],
    ["chickadee", "chocolate cake"],
    ["brown bear", "bear claw"],
  ];
  for (let i = 0; i < testCases.length; i++) {
    const result = feast(testCases[i][0], testCases[i][1]);
    console.log(`Test Case #${i + 1}: ${result}`);
  }
}

test();
