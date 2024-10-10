// https://www.codewars.com/kata/517abf86da9663f1d2000003

function toCamelCase(str) {
  const output = [];
  let capitalize = false;
  for (let chr of str) {
    if (chr == "-" || chr == "_") capitalize = true;
    else {
      output.push(capitalize ? chr.toUpperCase() : chr);
      capitalize = false;
    }
  }
  return output.join("");
}
