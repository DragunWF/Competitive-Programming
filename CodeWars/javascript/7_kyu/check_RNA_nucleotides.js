// https://www.codewars.com/kata/5a3325b4b6486ab367000064/train/javascript

function checkNucleotides(sequence) {
  const validLetters = ["A", "G", "C", "U"];
  for (let i = 0; i < sequence.length; i++) {
    const letter = sequence[i];
    if (!validLetters.includes(letter)) {
      return `There is an invalid letter: ${letter}. At position: ${i + 1}`;
    }
  }
  return `Valid Sequence: ${sequence}`;
}
