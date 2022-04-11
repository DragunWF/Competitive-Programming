// https://www.codewars.com/kata/581e476d5f59408553000a4b

function length(head) {
  let total = 0;
  while (true) {
    if (!head) break;
    head = head.next;
    total++;
  }
  return total;
}
