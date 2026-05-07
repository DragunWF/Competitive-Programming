// https://www.codewars.com/kata/581e50555f59405743001813/train/javascript

function anyMatch(head, p) {
  let currentNode = head;
  while (currentNode) {
    if (p(currentNode.data)) return true;
    currentNode = currentNode.next;
  }
  return false;
}

function allMatch(head, p) {
  let currentNode = head;
  while (currentNode) {
    if (!p(currentNode.data)) return false;
    currentNode = currentNode.next;
  }
  return true;
}
