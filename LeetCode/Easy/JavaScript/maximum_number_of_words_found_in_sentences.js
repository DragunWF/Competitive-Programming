// https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

/**
 * @param {string[]} sentences
 * @return {number}
 */
var mostWordsFound = function (sentences) {
  let maxWordCount = 0;
  for (let sentence of sentences) {
    const wordCount = sentence.split(" ").length;
    if (wordCount > maxWordCount) {
      maxWordCount = wordCount;
    }
  }
  return maxWordCount;
};
