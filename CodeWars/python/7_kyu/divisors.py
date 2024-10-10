# https://www.codewars.com/kata/544aed4c4a30184e960010f4

def divisors(integer):
    divisors = [i for i in range(2, integer) if integer % i == 0]
    return divisors if divisors else f"{integer} is prime"