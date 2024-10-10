// https://www.codewars.com/kata/580751a40b5a777a200000a1/train/javascript

function vowelOne(s) {
  const vowels = "aeiou";
  let output = "";
  for (let char of s.toLowerCase()) {
    output += vowels.includes(char) ? "1" : "0";
  }
  return output;
}
