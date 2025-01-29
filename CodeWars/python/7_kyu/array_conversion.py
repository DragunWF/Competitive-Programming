# https://www.codewars.com/kata/588854201361435f5e0000bd/train/python

def array_conversion(arr: list[int]) -> int:
    iteration = 1
    current = [*arr]
    temp = []

    while len(current) > 1:
        is_product = iteration % 2 == 0
        for i in range(0, len(current), 2):
            if is_product:
                temp.append(current[i] * current[i + 1])
            else:
                temp.append(current[i] + current[i + 1])
        current = [*temp]
        temp = []
        iteration += 1

    return current[0]


def test() -> None:
    print(array_conversion([1, 2, 3, 4, 5, 6, 7, 8]))


if __name__ == "__main__":
    test()
