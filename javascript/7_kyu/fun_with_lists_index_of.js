// https://www.codewars.com/kata/581c6b075cfa83852700021f

function indexOf(head, value) {
  const array = [];
  while (true) {
    if (!head) break;
    array.push(head.data);
    head = head.next;
  }
  return array.indexOf(value);
}
