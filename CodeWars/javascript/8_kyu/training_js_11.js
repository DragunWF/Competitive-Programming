// https://www.codewars.com/kata/5721c189cdd71194c1000b9b/train/javascript

function grabDoll(dolls) {
  let bag = []; // continue
  for (let doll of dolls) {
    if (doll === "Hello Kitty" || doll === "Barbie doll") {
      bag.push(doll);
    }
    if (bag.length === 3) {
      break;
    }
  }
  return bag; 
}
