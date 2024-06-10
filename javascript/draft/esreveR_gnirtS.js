// https://www.codewars.com/kata/52b74e0936d582d9210005ff/train/javascript

String.prototype.reverse = () => {
  let output = "";
  console.log(String(this));
  for (let str = this.toString(), i = str.length - 1; i >= 0; i--) {
    output += str[i];
  }
  return this.substring(0);
};

// Not part of the solution, just testing
function test() {
  console.log("Hello there".reverse());
}

test();
