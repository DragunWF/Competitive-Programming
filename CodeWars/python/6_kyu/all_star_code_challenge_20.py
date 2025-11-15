# https://www.codewars.com/kata/5865a75da5f19147370000c7

def add_arrays(array1: list, array2: list) -> list:
    if len(array1) != len(array2):
        raise Exception("Lengths are not equal")
    output = []
    for i in range(len(array1)):
        output.append(array1[i] + array2[i])
    return output


def test() -> None:
    print(add_arrays([1, 2], [4, 5]))  # // => [5,7]
    print(add_arrays([1, 2, 3], [4, 5]))  # // => Error


if __name__ == "__main__":
    test()
