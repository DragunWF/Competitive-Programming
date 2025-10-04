# https://www.codewars.com/kata/5b6d065a1db5ce9b4c00003c/train/python

from math import sqrt


def dropzone(fire: list[int, int], dropzones: list[list[int, int]]) -> list[int, int]:
    min_distance = None
    min_vector = []
    for vector in dropzones:
        distance = sqrt(((fire[0] - vector[0]) ** 2) +
                        ((fire[1] - vector[1]) ** 2))
        if min_distance is None or distance < min_distance:
            min_vector = vector
            min_distance = distance
    return min_vector


def test() -> None:
    # Expected: [0, 1]
    print(dropzone([1, 1], [[0, 1], [1, 0], [2, 2]]))

    # Expected: [7, 9]
    print(dropzone([6, 8], [[3, 2], [6, 1], [7, 9]]))

    # Expected: [1, -3]
    print(dropzone([1, -1], [[1, -3], [-2, 3], [0, 2]]))

    # Expected: [5, 5]
    print(dropzone([9, 2], [[1, 4], [9, 9], [5, 5]]))


if __name__ == "__main__":
    test()
