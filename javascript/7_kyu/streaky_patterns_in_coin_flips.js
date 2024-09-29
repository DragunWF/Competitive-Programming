// https://www.codewars.com/kata/5c1ac4f002c59c725900003f/train/javascript

/**
 * Checks if a sequence of coin flips has a specific streak pattern.
 * @param {string} sequence The sequence of coin flips, where 'H' is heads and 'T' is tails.
 * @param {number} l Length of each streak.
 * @param {number} n Number of streaks in the sequence.
 * @returns {boolean} `true` if the sequence has the pattern, `false` otherwise.
 */
function checkSequence(sequence, l, n) {
  let streaks = 0,
    seqLength = 1,
    lastChar = "";

  for (let char of sequence) {
    if (char !== lastChar) {
      if (seqLength === l) streaks++;
      lastChar = char;
      seqLength = 1;
    } else {
      seqLength++;
    }
  }
  if (seqLength === l) streaks++;

  return streaks === n;
}

function test() {
  // Not part of the solution, just testing
  console.log(checkSequence("THTTH", 2, 1)); // true
  console.log(checkSequence("TT", 2, 1)); // true
}

test();
