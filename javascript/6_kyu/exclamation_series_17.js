// https://www.codewars.com/kata/57fb44a12b53146fe1000136

function check_weight(scale) {
  return scale.split("").reduce((a, b) => {
    return b === "?" ? a + 3 : a + 2;
  }, 0);
}

function balance(left, right) {
  left = check_weight(left);
  right = check_weight(right);
  if (left === right) return "Balance";
  return left > right ? "Left" : "Right";
}
