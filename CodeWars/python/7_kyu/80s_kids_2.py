# https://www.codewars.com/kata/80-s-kids-number-2-help-alf-find-his-spaceship

from typing import Union


def find_spaceship(astromap: str) -> Union[list[int, int], str]:
    if not "X" in astromap:
        return "Spaceship lost forever."
    rows = astromap.split("\n")
    rows.reverse()
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if rows[i][j] == "X":
                return [j, i]


def test() -> None:
    # Expected: [0, 0]
    print(find_spaceship(".......\nX......."))


if __name__ == "__Main__":
    test()
