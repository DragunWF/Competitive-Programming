// https://www.codewars.com/kata/550f22f4d758534c1100025a/train/javascript

function dirReduc(arr) {
  const dir = { x: ["EAST", "WEST"], y: ["NORTH", "SOUTH"] };

  while (true) {
    const reducedDir = [];
    let repeat = false;
    let obseleteDir = false;

    for (let i = 0; i < arr.length; i++) {
      if (!obseleteDir) {
        for (let axis in dir) {
          if (
            dir[axis].includes(arr[i]) &&
            dir[axis].includes(arr[i + 1]) &&
            arr[i] !== arr[i + 1]
          ) {
            repeat = true;
            obseleteDir = true;
            break;
          }
        }
        if (!obseleteDir) reducedDir.push(arr[i]);
      } else obseleteDir = false;
    }

    if (!repeat) break;
    arr = reducedDir;
  }

  return arr;
}

console.log(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"])); // => []
console.log(
  dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
); // => ["WEST"]
console.log(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"])); // => ["NORTH", "WEST", "SOUTH", "EAST"]
console.log(dirReduc(["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"])); // => ["WEST", "WEST"]
console.log(dirReduc(["NORTH", "SOUTH", "EAST", "WEST", "EAST", "WEST"])); // => [];

// console.log(dirReduc(["EAST", "EAST", "NORTH", "WEST"])); // => ['EAST', 'NORTH']

// function dirReduc(arr) {
//   if (arr == ["NORTH", "WEST", "SOUTH", "EAST"]) return arr;

//   const directions = { NORTH: 1, SOUTH: -1, EAST: 1, WEST: -1 };
//   const reducedDir = [];
//   let xPos = 0;
//   let yPos = 0;

//   for (let direction of arr) {
//     if (direction == "WEST" || direction == "EAST")
//       xPos += directions[direction];
//     else yPos += directions[direction];
//   }
//   // console.log(`x: ${xPos} y: ${yPos}`);

//   if (xPos != 0) reducedDir.push(...addDir(xPos, ["WEST", "EAST"]));
//   if (yPos != 0) reducedDir.push(...addDir(yPos, ["SOUTH", "NORTH"]));
//   return reducedDir;
// }

// function addDir(axis, dir) {
//   const output = [];
//   for (let i = 0; i < Math.abs(axis); i++) {
//     if (axis > 0) output.push(dir[1]);
//     if (axis < 0) output.push(dir[0]);
//   }
//   return output;
// }
