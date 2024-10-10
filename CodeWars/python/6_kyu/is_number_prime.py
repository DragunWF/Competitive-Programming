# https://www.codewars.com/kata/5262119038c0985a5b00029f

def is_prime(num):
    if num > 1:
        for x in range(2, 100000):
            if ((num % x) == 0) and not num == x:
                return False
        return True
    else:
        return False

# Yes I know, I brute-forced it when I shouldn't have. I'm going to
# be redoing this at some point in the future but with better code.
