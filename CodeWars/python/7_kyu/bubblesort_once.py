# https://www.codewars.com/kata/56b97b776ffcea598a0006f2/train/python

def bubblesort_once(l: list[int]) -> list[int]:
    output = l.copy()
    for i in range(len(output) - 1):
        if output[i] > output[i + 1]:
            output[i], output[i + 1] = output[i + 1], output[i]
    return output


def test() -> None:
    # Expected: [7, 5, 3, 1, 2, 4, 6, 8, 9]
    print(bubblesort_once([9, 7, 5, 3, 1, 2, 4, 6, 8]))


if __name__ == "__main__":
    test()
