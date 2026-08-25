// https://www.codewars.com/kata/5f55ecd770692e001484af7d/train/javascript

function mirror(data) {
  if (!data.length) {
    return [];
  }
  const dataCopy = [...data];
  dataCopy.sort((a, b) => a - b);
  const maxElement = dataCopy[dataCopy.length - 1];
  const ascendingHalf = dataCopy.slice(0, -1);
  const descendingHalf = [...ascendingHalf];
  descendingHalf.reverse();
  return [...ascendingHalf, maxElement, ...descendingHalf];
}
