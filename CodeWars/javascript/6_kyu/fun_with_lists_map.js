// https://www.codewars.com/kata/58259d9062cfb45e1a00006b/train/javascript

function Node(data, next = null) {
  this.data = data;
  this.next = next;
}

function map(head, f) {
  if (!head) return null;

  const newHead = new Node();
  let tempNode = newHead;
  let currentNode = head;
  while (currentNode) {
    tempNode.data = f(currentNode.data);
    tempNode.next = currentNode.next ? new Node() : null;
    currentNode = currentNode.next;
    tempNode = tempNode.next;
  }
  return newHead;
}
