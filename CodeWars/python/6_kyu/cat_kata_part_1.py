# https://www.codewars.com/kata/5869848f2d52095be20001d1/train/python

from math import sqrt


def peaceful_yard(yard: list[list[str]], min_distance: int) -> bool:
    CATS = "LMR"
    positions = []
    for i, row in enumerate(yard):
        for j, char in enumerate(row):
            if char in CATS:
                positions.append([i, j])
    if len(positions) <= 1:
        return True
    return identify_confict(positions, min_distance)


def identify_confict(positions: list[int], min_distance: int) -> bool:
    for i, position in enumerate(positions):
        for j, otherPosition in enumerate(positions):
            if i == j:
                continue
            x_distance = abs(position[0] - otherPosition[0]) ** 2
            y_distance = abs(position[1] - otherPosition[1]) ** 2
            if sqrt(x_distance + y_distance) < min_distance:
                return False
    return True


def test() -> None:
    # Expected: True
    print(peaceful_yard(["------------",
                         "------------",
                         "-L----------",
                         "------------",
                         "------------",
                         "------------"], 10))
    # Expected: False
    print(peaceful_yard(["------------",
                         "---M--------",
                         "------------",
                         "------------",
                         "-------R----",
                         "------------"], 6))
    # Expected: True
    print(peaceful_yard(["-----------L",
                         "--R---------",
                         "------------",
                         "------------",
                         "------------",
                         "--M---------"], 4))

    # Expected: False
    print(peaceful_yard(['------------',
                         '--L-------R-',
                         '----M-------',
                         '------------',
                         '------------',
                         '------------'], 6))

    # Expected: True
    print(peaceful_yard(['------------', '--L---R---M-', '------------',
          '------------', '------------', '------------'], 2))


if __name__ == "__main__":
    test()
