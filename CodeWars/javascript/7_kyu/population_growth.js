// https://www.codewars.com/kata/563b662a59afc2b5120000c6/train/javascript

function nbYear(p0, percent, aug, p) {
  let years = 0;
  while (p0 < p) {
    years++;
    p0 += Math.floor(p0 * percent * 0.01 + aug);
  }
  return years;
}

// Not part of the solution
function test() {
  const testCases = [
    { p0: 1500, percent: 5, aug: 100, p: 5000 },
    { p0: 1500000, percent: 2.5, aug: 10000, p: 2000000 },
    { p0: 1500000, percent: 0.25, aug: 1000, p: 2000000 },
    { p0: 1000, percent: 2, aug: 50, p: 1214 },
  ];
  for (let i = 0; i < testCases.length; i++) {
    const nth = i + 1;
    const result = nbYear(
      testCases[i].p0,
      testCases[i].percent,
      testCases[i].aug,
      testCases[i].p
    );
    console.log(`Test Case #${nth}: ${result}`);
  }
}

test();
