// https://www.codewars.com/kata/53a8beaca9198e77b9000309/train/javascript

// arr.filter(Boolean) would have been faster

function squeakyClean(arr) {
  return arr.filter((item) => Boolean(item));
}
