// https://www.codewars.com/kata/583ef2456e39941f810001c5/train/python

function duplicateOrUnique(arr) {
  const counts = {};

  for (let num of arr) {
    if (num in counts) {
      counts[num] += 1;
    } else {
      counts[num] = 1;
    }
  }

  const uniqueNumbers = [];
  const duplicateNumbers = [];

  for (let num of Object.keys(counts)) {
    const count = counts[num];
    if (count === 1) {
      uniqueNumbers.push(Number(num));
    } else {
      duplicateNumbers.push(Number(num));
    }
    if (uniqueNumbers.length > 1 && duplicateNumbers === 1) {
      return duplicateNumbers[0];
    }
    if (duplicateNumbers.length > 1 && uniqueNumbers.length === 1) {
      return uniqueNumbers[0];
    }
  }

  return uniqueNumbers.length === 1 ? uniqueNumbers[0] : duplicateNumbers[0];
}
