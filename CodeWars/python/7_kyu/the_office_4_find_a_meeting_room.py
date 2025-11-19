# https://www.codewars.com/kata/57f604a21bd4fe771b00009c

from typing import Union


def meeting(rooms: list[str]) -> Union[str, int]:
    for i, status in enumerate(rooms):
        if status == "O":
            return i
    return "None available!"


def test() -> None:
    # Expected: 0
    print(meeting(['O', 'X', 'X', 'X', 'X']))


if __name__ == "__main__":
    test()
