# https://www.codewars.com/kata/5300901726d12b80e8000498/train/python

def fizzbuzz(n) -> list:
    return [convert(i) for i in range(1, n + 1)]


def convert(n) -> int:
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return n
