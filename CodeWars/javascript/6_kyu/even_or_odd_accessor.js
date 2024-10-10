// https://www.codewars.com/kata/6656a4687f3e4eb5fb520817/train/javascript

const evenOrOdd = new Proxy((n) => (n % 2 === 0 ? "Even" : "Odd"), {
  get: (target, prop) => {
    return target(Number(prop));
  },
});

// Not part of the solution, just testing
function test() {
  console.log(evenOrOdd(2));
  console.log(evenOrOdd[2]);
}

test();
