# https://www.codewars.com/kata/57faece99610ced690000165/train/python

def remove(s: str) -> str:
    last_exclamation_index = None
    for i in range(len(s) - 1, -1, -1):
        if s[i] != "!":
            last_exclamation_index = i
            break
    return s[0:last_exclamation_index + 1]


def test():
    # Not part of the solution, just testing
    print(remove("Hi! Hi!! Hi"))


if __name__ == "__main__":
    test()
