// https://www.codewars.com/kata/55beec7dd347078289000021/train/javascript

function Node(data) {
  this.data = data;
  this.next = null;
}

function length(head) {
  let length = 0;
  for (let node = head; node !== null; node = node.next) {
    length++;
  }
  return length;
}

function count(head, data) {
  let count = 0;
  for (let node = head; node !== null; node = node.next) {
    if (node.data === data) {
      count++;
    }
  }
  return count;
}
