// https://www.codewars.com/kata/581c867a33b9fe732e000076

function count(array, element) {
  let total = 0;
  for (let x of array) if (x === element) total++;
  return total;
}

function lastIndexOf(head, value) {
  if (!head) return -1;
  const array = [];
  while (true) {
    array.push(head.data);
    if (head.next) head = head.next;
    else break;
  }
  while (count(array, value) > 1) array[array.indexOf(value)] = NaN;
  return array.indexOf(value);
}
