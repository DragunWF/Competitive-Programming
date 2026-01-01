// https://www.codewars.com/kata/58dd98fe8d29b0f30d0002bd/train/javascript

function objectType(obj) {
  return arguments.length
    ? Object.prototype.toString.call(obj)
    : "[object Null]";
}
