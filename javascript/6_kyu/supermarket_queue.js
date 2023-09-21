// https://www.codewars.com/kata/57b06f90e298a7b53d000a86

function queueTime(customers, n) {
  if (!customers.length) return 0;
  if (n >= customers.length) return getMax(customers);
  if (n === 1) return customers.reduce((a, b) => a + b, 0);
  return simulateQueue(customers, n);
}

function simulateQueue(customers, n) {
  let queue = [];
  let totalTime = 0;
  for (let i = 0; i < customers.length; i++) {
    queue.push(customers[i]);
    while (
      queue.length === n ||
      (i + 1 === customers.length && queue.length !== 0)
    ) {
      queue = queue.map((x) => x - 1);
      totalTime++;
      const indiciesToRemove = [];
      for (let j = 0; j < queue.length; j++) {
        if (queue[j] <= 0) {
          indiciesToRemove.push(j);
        }
      }
      if (indiciesToRemove.length) {
        queue = renewQueue(queue, indiciesToRemove);
      }
    }
  }
  return totalTime;
}

function getMax(arr) {
  let max = arr[0];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > max) {
      max = arr[i];
    }
  }
  return max;
}

function renewQueue(queue, excludedIndices) {
  const output = [];
  for (let i = 0; i < queue.length; i++) {
    if (!excludedIndices.includes(i)) {
      output.push(queue[i]);
    }
  }
  return output;
}

// Not part of the solution
function test() {
  console.log(queueTime([5, 3, 4], 1));
  // should return 12
  // because when there is 1 till, the total time is just the sum of the times

  console.log(queueTime([10, 2, 3, 3], 2));
  // should return 10
  // because here n=2 and the 2nd, 3rd, and 4th people in the
  // queue finish before the 1st person has finished.

  console.log(queueTime([2, 3, 10], 2));
  // should return 12

  console.log(queueTime([2, 2, 3, 3, 4, 4], 2));
  // should return 9

  console.log(queueTime([1, 2, 3, 4, 5], 100));
  // should return 5
}

test();
