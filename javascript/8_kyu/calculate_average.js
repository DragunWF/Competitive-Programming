// https://www.codewars.com/kata/57a2013acf1fa5bfc4000921

function find_average(array) {
  if (!array.length > 0) return 0;
  let total = array.reduce((a, b) => {
    return a + b;
  });
  return total / array.length;
}
