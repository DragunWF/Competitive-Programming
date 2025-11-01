// https://www.codewars.com/kata/52dd72494367608ac1000416/train/javascript

function isPrime(number) {
  if (number <= 1) return false;
  if (number === 2) return true;
  for (let i = 2; i < Math.sqrt(number) + 1; i++) {
    if (number % i === 0) {
      return false;
    }
  }
  return true;
}

function getPrimes(start, finish) {
  const primes = [];
  if (finish > start) {
    for (let i = start; i <= finish; i++) {
      if (isPrime(i)) primes.push(i);
    }
  } else {
    for (let i = start; i >= finish; i--) {
      if (isPrime(i)) primes.push(i);
    }
    primes.sort((a, b) => a - b);
  }
  return primes;
}

function test() {
  console.log(isPrime(0)); // === false
  console.log(isPrime(1)); // === false
  console.log(isPrime(2)); // === true
  console.log(isPrime(3)); // === true
  console.log(isPrime(4)); // === false
  console.log(isPrime(5)); // === true

  console.log(getPrimes(0, 0)); // === []
  console.log(getPrimes(0, 30)); // === [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
  console.log(getPrimes(30, 0)); // === [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
}

test();
