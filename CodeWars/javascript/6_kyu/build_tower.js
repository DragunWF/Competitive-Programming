// https://www.codewars.com/kata/576757b1df89ecf5bd00073b

function towerBuilder(nFloors) {
  const output = [];
  const rowLength = nFloors * 2 - 1;
  let stars = 1;
  for (let i = 0; i < nFloors; i++) {
    const sideLength = Math.ceil(rowLength / 2) - stars + i;
    output.push(generateFloor(stars, sideLength));
    stars += 2;
  }
  return output;
}

function generateFloor(mid, side) {
  let output = "";
  for (let i = 0; i < 2; i++) {
    for (let j = 1; j <= side; j++) {
      output += " ";
    }
    if (i === 0) {
      for (let j = 0; j < mid; j++) {
        output += "*";
      }
    }
  }
  return output;
}

// Not part of the solution
function test() {
  const testCasesEnd = 10;
  for (let i = 6; i <= testCasesEnd; i++) {
    console.log(towerBuilder(i));
  }
}

test();
