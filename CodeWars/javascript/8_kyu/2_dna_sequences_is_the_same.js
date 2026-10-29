// https://www.codewars.com/kata/57cbb9e240e3024aae000b26/train/javascript

const codons = {}; // codons is a prebuilt object in the kata

function codeForSameProtein(seq1, seq2) {
  const dnaSeq = {
    seq1: [],
    seq2: [],
  };
  let dna1 = "";
  let dna2 = "";
  for (let i = 0, nth = 1; i < seq1.length; i++, nth++) {
    dna1 += seq1[i];
    dna2 += seq2[i];
    if (nth % 3 === 0) {
      dnaSeq.seq1.push(codons[dna1]);
      dnaSeq.seq2.push(codons[dna2]);
      dna1 = "";
      dna2 = "";
    }
  }
  return dnaSeq.seq1.join("") === dnaSeq.seq2.join("");
}
