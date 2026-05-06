// https://www.codewars.com/kata/58319f37aeb69a89a00000c7

function reduce(head, f, init) {
  if (!head) return init;

  const initialHead = head;
  let currentNode = initialHead;
  let output = init;
  while (currentNode) {
    output = f(output, currentNode.data);
    currentNode = currentNode.next;
  }
  return output;
}
