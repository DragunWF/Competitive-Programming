// https://www.codewars.com/kata/554e4a2f232cdd87d9000038/

function DNAStrand(dna) {
  let output = "";
  for (let character of dna) {
    if (character === "A" || character === "T") {
      output += character === "A" ? "T" : "A";
    }
    if (character === "C" || character === "G") {
      output += character === "C" ? "G" : "C";
    }
  }
  return output;
}

// Not part of the solution
function test() {
  const testCases = ["ATTGC", "GTAT"];
  for (let i = 0; i < testCases.length; i++) {
    const result = DNAStrand(testCases[i]);
    console.log(`Test Case #${i + 1}: ${result}`);
  }
}

test();
