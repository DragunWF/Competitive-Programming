// https://www.codewars.com/kata/5f25f475420f1b002412bb1f/train/javascript

function findTheNumberPlate(customerID) {
  const id = customerID + 1;

  let carPlateNum = id % 999 === 0 ? 999 : id % 999;
  if (carPlateNum < 10) carPlateNum = `00${carPlateNum}`;
  else if (carPlateNum < 100) carPlateNum = `0${carPlateNum}`;

  const firstLetter = getAlphabet(customerID, 999);
  const secondLetter = getAlphabet(customerID, 999 * 26);
  const thirdLetter = getAlphabet(customerID, 999 * 26 * 26);

  return `${firstLetter}${secondLetter}${thirdLetter}${carPlateNum}`;
}

function getAlphabet(id, divisor) {
  const alphabets = "abcdefghijklmnopqrstuvwxyz";
  let index = Math.floor(id / divisor);
  if (index >= alphabets.length) index %= alphabets.length;
  return alphabets[index];
}

console.log(findTheNumberPlate(3)); // aaa004
console.log(findTheNumberPlate(1487)); // baa489
console.log(findTheNumberPlate(40000)); // oba041
console.log(findTheNumberPlate(17558423)); // zzz999
console.log(findTheNumberPlate(234567)); // aja802
console.log(findTheNumberPlate(43056)); // rba100
