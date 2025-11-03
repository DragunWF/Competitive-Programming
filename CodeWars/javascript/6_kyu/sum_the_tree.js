// https://www.codewars.com/kata/5800580f8f7ddaea13000025/train/javascript

function sumTheTreeValues(root) {
  let total = 0;
  function inorderTraversal(node) {
    if (!node) return;
    inorderTraversal(node.left);
    total += node.value;
    inorderTraversal(node.right);
  }
  inorderTraversal(root);
  return total;
}

function test() {
  var simpleNode = {
    value: 10,
    left: { value: 1, left: null, right: null },
    right: { value: 2, left: null, right: null },
  };
  console.log(sumTheTreeValues(simpleNode)); // 13
}

test();
