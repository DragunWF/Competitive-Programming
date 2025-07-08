# https://www.codewars.com/kata/58989a079c70093f3e00008d/train/python

from itertools import product


def cartesian_neighbor(x: int, y: int) -> list:
    neighbors = list(product([x - 1, x, x + 1], [y - 1, y, y + 1]))
    for i, pair in enumerate(neighbors):
        if pair[0] == x and pair[1] == y:
            neighbors.pop(i)
            break
    return neighbors


def test() -> None:
    # [(1,1),(1,2),(1,3),(2,1),(2,3),(3,1),(3,2),(3,3)]
    print(cartesian_neighbor(2, 2))
    # [(6,7),(6,6),(6,8),(4,7),(4,6),(4,8),(5,6),(5,8)]
    print(cartesian_neighbor(5, 7))


if __name__ == "__main__":
    test()
