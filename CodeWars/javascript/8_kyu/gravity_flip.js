// https://www.codewars.com/kata/5f70c883e10f9e0001c89673

const flip = (d, a) => {
  a = a.sort((a, b) => a - b);
  return d === "R" ? a : a.reverse();
};
