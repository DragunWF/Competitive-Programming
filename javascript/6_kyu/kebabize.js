// https://www.codewars.com/kata/57f8ff867a28db569e000c4a

function kebabize(str) {
  const letters = "abcdefghijklmnopqrstuvwxyz";
  let output = "";
  for (let i = 0; i < str.length; i++) {
    if (!letters.includes(str[i].toLowerCase())) continue;
    if (str[i] === str[i].toUpperCase()) {
      output += i !== 0 ? `-${str[i].toLowerCase()}` : str[i].toLowerCase();
    } else {
      output += str[i];
    }
  }
  return output;
}

// test code
console.log(kebabize("MyCamelCasedString"));
console.log(kebabize("CAMEL"));
