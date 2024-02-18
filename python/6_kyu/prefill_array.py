# https://www.codewars.com/kata/54129112fb7c188740000162/train/python

def prefill(n, v):
    try:
        return [v for i in range(int(n))]
    except (TypeError, ValueError):
        return f"{n} is invalid"


# (f"{v} " * n).rstrip().split(" ")
# test code
print(prefill(3, 1))
print(prefill(0, 1))
