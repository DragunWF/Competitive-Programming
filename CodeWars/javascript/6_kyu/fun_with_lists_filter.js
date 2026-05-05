// https://www.codewars.com/kata/582041237df353e01d000084/train/javascript

function Node(data, next = null) {
  this.data = data;
  this.next = next;
}

function filter(head, p) {
  if (!head) return null;

  const newHead = new Node();
  let tempNode = newHead;
  let prevNode = null;
  let currentNode = head;
  let length = 0;
  while (currentNode) {
    if (p(currentNode.data)) {
      length++;
      prevNode = tempNode;
      tempNode.data = currentNode.data;
      tempNode.next = currentNode.next ? new Node() : null;
      tempNode = tempNode.next;
    }
    currentNode = currentNode.next;
  }
  if (prevNode?.next && !prevNode.next?.data) {
    prevNode.next = null;
  }
  if (!length) {
    return null;
  }
  return newHead;
}
