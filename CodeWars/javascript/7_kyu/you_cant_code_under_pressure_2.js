// https://www.codewars.com/kata/5546ea9bddfc5c0c38000026/train/javascript

function Counter() {
  let count = 0;
  this.check = () => {
    return count;
  };
  this.increment = () => {
    count++;
  };
}
