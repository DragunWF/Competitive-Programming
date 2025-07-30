# https://www.codewars.com/kata/55491e9e50f2fc92f3000074/train/python

from string import ascii_uppercase


def ride(group: str, comet: str) -> str:
    positions = get_positions()
    group_value = get_value(group, positions)
    comet_value = get_value(comet, positions)
    return "GO" if group_value == comet_value else "STAY"


def get_positions() -> dict:
    positions = {}  # For O(1) time complexity in retrieval
    for i, char in enumerate(ascii_uppercase):
        positions[char] = i + 1
    return positions


def get_value(s: str, positions: dict) -> int:
    product = 1
    for char in s:
        product *= positions[char]
    return product % 47


def test() -> None:
    print(ride("COMETQ", "HVNGAT"))  # "GO"
    print(ride("CAMETQ", "HVNADT"))  # "STAY"


if __name__ == "__main__":
    test()
