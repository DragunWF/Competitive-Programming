// https://www.codewars.com/kata/5267faf57526ea542e0007fb

function splitPoint(value) {
  return value.toString().split(".");
}

function convert(value) {
  return Number(splitPoint(value)[0]);
}

Math.ceil = (number) => {
  if (splitPoint(number).length === 1) return number;
  return convert(number) + 1;
};

Math.floor = (number) => {
  return convert(number);
};

Math.round = (number) => {
  const arr = splitPoint(number);
  if (arr.length === 1) return number;
  return Number(arr[1][0]) >= 5 ? Math.ceil(number) : Math.floor(number);
};

// Not part of the solution
console.log(Math.ceil(0));
