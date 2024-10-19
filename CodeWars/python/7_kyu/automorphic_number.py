# https://www.codewars.com/kata/5a58d889880385c2f40000aa/train/python

def automorphic(n: int) -> str:
    return "Automorphic" if str(n) == str(n * n)[-len(str(n)):] else "Not!!"
