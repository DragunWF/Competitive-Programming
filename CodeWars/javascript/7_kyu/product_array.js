// https://www.codewars.com/kata/5a905c2157c562994900009d

function productArray(numbers) {
  const output = [];
  for (let i = 0; i < numbers.length; i++) {
    let product = 1;
    for (let j = 0; j < numbers.length; j++) {
      if (i === j) continue;
      product *= numbers[j];
    }
    output.push(product);
  }
  return output;
}

// Test code
console.log(productArray([1, 5, 2]));
