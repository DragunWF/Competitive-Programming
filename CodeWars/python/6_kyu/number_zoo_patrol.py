# https://www.codewars.com/kata/5276c18121e20900c0000235/train/python

def find_missing_number(numbers: list[int]):
    n = len(numbers) + 1
    return int(((n * (n + 1)) / 2) - sum(numbers))


def test():
    # Not part of the solution, just testing
    print(find_missing_number([1, 2, 3, 4]))


if __name__ == "__main__":
    test()
