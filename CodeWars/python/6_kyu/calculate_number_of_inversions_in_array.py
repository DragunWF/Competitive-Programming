# https://www.codewars.com/kata/537529f42993de0e0b00181f

def count_inversions(array: list[int]) -> int:
    inversions = 0
    for i in range(len(array) - 1):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                inversions += 1
                array[j], array[j + 1] = array[j + 1], array[j]
    return inversions


def test() -> None:
    print(count_inversions([1, 2, 3, 4]))


if __name__ == "__main__":
    test()
