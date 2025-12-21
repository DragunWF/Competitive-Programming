# https://www.codewars.com/kata/5906436806d25f846400009b/train/python

import math


def x(n: int):
    lines = []
    edge_char_count = 0
    half = math.ceil(n / 2)
    middle_char_count = n - 2
    for i in range(1, n + 1):
        edges = "□" * edge_char_count
        middle = "□" * middle_char_count
        if i == half:
            lines.append(f"{edges}■{edges}")
        else:
            lines.append(f"{edges}■{middle}■{edges}")
        if i >= half:
            edge_char_count -= 1
            middle_char_count += 2
        else:
            edge_char_count += 1
            middle_char_count -= 2
    return "\n".join(lines)


def test() -> None:
    # This is just for testing and it is not part of the solution
    print(x(3))
    print(x(5))


if __name__ == "__main__":
    test()
