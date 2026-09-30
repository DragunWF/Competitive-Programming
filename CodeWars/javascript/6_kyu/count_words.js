// https://www.codewars.com/kata/56b3b27cadd4ad275500000c/train/javascript

function wordCount(s) {
  const words = s.toLowerCase().split(/[^a-zA-Z]+/);
  const exceptions = ["a", "the", "on", "at", "of", "upon", "in", "as"];
  let filteredWordCount = 0;
  for (let word of words) {
    if (word.length > 0 && !exceptions.includes(word)) {
      filteredWordCount++;
    }
  }
  return filteredWordCount;
}
