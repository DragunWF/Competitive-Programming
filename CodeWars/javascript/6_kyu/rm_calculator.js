// https://www.codewars.com/kata/595bbea8a930ac0b91000130

function calculate1RM(w, r) {
  if (r === 1) return w;
  if (!r) return 0;
  return Math.round(
    Math.max(w * (1 + r / 30), (100 * w) / (101.3 - 2.67123 * r), w * r ** 0.1)
  );
}

// Not part of the solution
function test() {
  const testCases = [
    [135, 20, 282],
    [200, 8, 253],
    [270, 2, 289],
    [360, 1, 360],
    [400, 0, 0],
  ];
  for (let i = 0; i < testCases.length; i++) {
    const result =
      calculate1RM(testCases[i][0], testCases[i][1]) === testCases[i][2];
    console.log(`Test Case #${i + 1}: ${result}`);
    if (!result) {
      console.log("Failed Case:", testCases[i]);
    }
  }
}

test();
