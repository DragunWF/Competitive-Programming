# https://www.codewars.com/kata/56f3a1e899b386da78000732/train/python

def partlist(arr: list[str]) -> list[list[str, str]]:
    output = []
    limit = 1
    for i in range(len(arr) - 1):
        output.append((concat(arr[0:limit + i]), 
                       concat(arr[limit + i: len(arr)])))
    return output


def concat(arr: list[str]) -> str:
    return " ".join(arr)


def test():
    # Not part of the solution, just testing
    print(partlist(["az", "toto", "picaro", "zone", "kiwi"]))


if __name__ == "__main__":
    test()