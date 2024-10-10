// https://www.codewars.com/kata/5819081d056d4bdd410004f8

function countIf(head, p) {
  const array = [];
  while (true) {
    if (!head) break;
    array.push(head.data);
    head = head.next;
  }
  return array.filter((x) => p(x)).length;
}
