// https://www.codewars.com/kata/53f9ee9f64b19d4b1d0001ed

function Warrior(n) {
  this.username = n;
  this.name = function (new_name = undefined) {
    if (new_name) this.username = new_name;
    return this.username;
  };
}

Warrior.prototype.toString = function () {
  return "Hi! my name's " + this.name();
};
