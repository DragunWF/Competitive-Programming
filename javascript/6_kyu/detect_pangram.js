// https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/javascript

function isPangram(string) {
  const alphabets = "abcdefghijklmnopqrstuvwxyz".split("");
  const uniqueCharacters = [...new Set(string.toLowerCase().split(""))].filter((x) => {
    return alphabets.includes(x);
  }).length;
  return uniqueCharacters == 26;
}
