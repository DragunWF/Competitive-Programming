# https://www.codewars.com/kata/5613d06cee1e7da6d5000055/train/python

def step(g: int, m: int, n: int) -> list[int]:
    seen_primes = []
    for number in range(m, n + 1):
        if is_prime(number):
            pair = find_pair(seen_primes, number, g)
            if pair:
                return pair
            seen_primes.append(number)


def find_pair(seen_primes: list[int], current_prime: int, g: int) -> list:
    if not seen_primes:
        return []
    for prime_number in seen_primes:
        if current_prime - prime_number == g:
            return [prime_number, current_prime]
    return []


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def test() -> None:
    # Expected: [101, 103]
    print(step(2, 100, 110))

    # Expected: [307, 317]
    print(step(10, 300, 400))


if __name__ == "__main__":
    test()
