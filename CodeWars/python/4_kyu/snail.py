# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python
from rich import print  # for testing purposes
from time import sleep


def snail(snail_map: list) -> list:
    right, down, left, up = True, False, False, False
    height, width = len(snail_map), len(snail_map[0])
    bool_map, output = [], []

    for j in range(height):
        bool_line = []
        for i in range(width):
            bool_line.append(False)
        bool_map.append(bool_line)

    j, i = 0, 0
    while not cleared(bool_map):
        output.append(snail_map[i][j])
        bool_map[i][j] = True
        # display_bool_map(bool_map)

        if right:
            j += 1
            if j + 1 >= width or bool_map[i][j + 1]:
                right = False
                down = True
        elif down:
            i += 1
            if i + 1 >= height or bool_map[j][i + 1]:
                down = False
                left = True
        elif left:
            j -= 1
            if j - 1 < 0 or bool_map[i][j - 1]:
                left = False
                up = True
        elif up:
            i -= 1
            if i - 1 < 0 or bool_map[i - 1][j]:
                up = False
                right = True
        # sleep(0.5)

    return output


def cleared(bool_map: list) -> bool:
    for line in bool_map:
        for tile in line:
            if not tile:
                return False
    return True


def test():
    test_cases = [
        [[1, 2, 3],
         [8, 9, 4],
         [7, 6, 5]],
        [[1, 2, 3, 1],
         [4, 5, 6, 4],
         [7, 8, 9, 7],
         [7, 8, 9, 7]]
    ]
    for case in test_cases:
        print(snail(case))


def display_bool_map(bool_map: list):
    for line in bool_map:
        print(line)
    print()


if __name__ == "__main__":
    test()
