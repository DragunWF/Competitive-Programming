// https://www.codewars.com/kata/5655c60db4c2ce0c2e000026/train/javascript

function compose(...args) {
  function func(n) {
    if (!args.length) return n;
    let composedFunc = args[args.length - 1](n);
    for (let i = args.length - 2; i >= 0; i--) {
      composedFunc = args[i](composedFunc);
    }
    return composedFunc;
  }
  return func;
}

function test() {
  const addOne = (a) => a + 1;
  const multTwo = (b) => b * 2;
  const addOneMultTwo = compose(multTwo, addOne);

  console.log(addOneMultTwo(5)); // returns 12
}

test();
