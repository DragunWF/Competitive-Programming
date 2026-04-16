# https://www.codewars.com/kata/56e3cd1d93c3d940e50006a4/train/python

def make_valley(arr: list[int]) -> list[int]:
    arr.sort(reverse=True)
    first_half = []
    second_half = []
    for i, num in enumerate(arr):
        if len(arr) % 2 != 0 and i == len(arr) - 1:
            break
        if i % 2 == 0:
            first_half.append(num)
        else:
            second_half.append(num)
    second_half.reverse()
    if len(arr) % 2 == 0:
        return [*first_half, *second_half]
    return [*first_half, arr[-1], *second_half]


def test() -> None:
    # Expected [79, 35, 25, 19, 35, 54]
    print(make_valley([79, 35, 54, 19, 35, 25]))

    # Expected: [100, 93, 67, -16, 65, 92, 97]
    print(make_valley([67, 93, 100, -16, 65, 97, 92]))


if __name__ == "__main__":
    test()

# [17, 14, 7, 5, 4, 1, 4, 7, 8, 15, 17]
# [17, 15, 8, 7, 4, 1, 4, 5, 7, 14, 17]
