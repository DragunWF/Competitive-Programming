// https://www.codewars.com/kata/5681bc8d17af37f50e000015/train/javascript

function primes(start, end) {
  const primeList = [];
  for (let n = start; n <= end; n++) {
    if (isPrime(n)) {
      primeList.push(n);
    }
  }
  return primeList.length > 0 ? primeList : null;
}

function isPrime(num) {
  if (num <= 1) return false;
  if (num <= 3) return true;
  if (num % 2 === 0 || num % 3 === 0) return false;

  for (let i = 5; i * i <= num; i += 6) {
    if (num % i === 0 || num % (i + 2) === 0) return false;
  }
  return true;
}
