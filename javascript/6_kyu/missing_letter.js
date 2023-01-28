// https://www.codewars.com/kata/5839edaa6754d6fec10000a2

function findMissingLetter(array) {
  const alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
  for (let i = 0; i < alphabets.length; i++) {
    if (alphabets[i] === array[0]) {
      for (let j = 0; j < array.length; j++) {
        if (alphabets[i + j] !== array[j]) {
          return alphabets[i + j];
        }
      }
    }
  }
}
