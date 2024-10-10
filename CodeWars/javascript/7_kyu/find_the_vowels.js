// https://www.codewars.com/kata/5680781b6b7c2be860000036/train/javascript

function vowelIndices(word) {
  const vowels = ["a", "e", "i", "o", "u", "y"];
  const indexes = [];
  for (let i = 0; i < word.length; i++)
    if (vowels.includes(word[i].toLowerCase())) 
      indexes.push(i + 1);
  return indexes;
}
