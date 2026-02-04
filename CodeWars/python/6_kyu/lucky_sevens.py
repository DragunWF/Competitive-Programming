# https://www.codewars.com/kata/58275b63083e128edb00098d/train/python


def lucky_sevens(arr: list[list]) -> int:
    count = 0
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if is_lucky_seven(arr, row, col):
                count += 1
    return count


def is_lucky_seven(arr: list[list], row: int, col: int) -> bool:
    if arr[row][col] != 7:
        return False
    adjacent_sum = get_adjacent_sum(arr, row, col)
    return is_perfect_cube(adjacent_sum)


def get_adjacent_sum(arr: list[list], row: int, col: int) -> int:
    total = 0
    if row + 1 < len(arr):
        total += arr[row + 1][col]
    if row - 1 >= 0:
        total += arr[row - 1][col]
    if col + 1 < len(arr[row]):
        total += arr[row][col + 1]
    if col - 1 >= 0:
        total += arr[row][col - 1]
    return total


def is_perfect_cube(n: int) -> bool:
    if n >= 0:
        cube_root = round(n ** (1 / 3))
        return cube_root ** 3 == n
    abs_n = abs(n)
    cube_root = round(abs_n ** (1 / 3))
    return -(cube_root ** 3) == n


def test() -> None:
    # Expected: 1
    print(lucky_sevens([['x', 513, 'x', 'x', 'x'],
                        [82, 7, 32, 'x', 'x'],
                        ['x', 102, 'x', 'x', 'x'],
                        ['x', 'x', 'x', 'x', 'x'],
                        ['x', 'x', 'x', 'x', 'x']]))

    # Expected: 4
    print(lucky_sevens([[647, 25, 530, 200, 438, 635],
                        [10, 7, 19, 17, 439, 7],
                        [271, 10, 3, 7, 5, 187],
                        [768, 430, 876, 2, 335, 57],
                        [21, 7, 229, 108, 7, 63],
                        [939, 49, 199, 611, 6, 513]]))


if __name__ == "__main__":
    test()
