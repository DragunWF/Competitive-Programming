// https://www.codewars.com/kata/525f4206b73515bffb000b21/train/javascript

function add(a, b) {
  return BigInt(String(Number(a) + Number(b)));
}

console.log(add("123", "321"));
