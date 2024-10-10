// https://www.codewars.com/kata/535c1c80cdbf5011e600030f

function KeywordCipher(abc, keyword) {
  const x = `${abc}`.split("");
  let y = "";
  keyword = removeDuplicates(keyword);
  for (c of x) if (!keyword.split("").includes(c)) y += c;
  y = `${keyword}${y}`.split("");
  this.encode = function (str) {
    let output = "";
    for (ch of str) {
      if (y.includes(ch)) output += y[x.indexOf(ch)];
      else output += ch;
    }
    return output;
  };
  this.decode = function (str) {
    let output = "";
    for (ch of str) {
      if (x.includes(ch)) output += x[y.indexOf(ch)];
      else output += ch;
    }
    return output;
  };
}

function removeDuplicates(string) {
  const uniques = [];
  const duplicates = [];
  for (ch of string) {
    if (!uniques.includes(ch)) uniques.push(ch);
    else duplicates.push(ch);
  }
  return uniques.join("");
}
