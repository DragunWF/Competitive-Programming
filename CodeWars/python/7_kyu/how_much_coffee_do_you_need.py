# https://www.codewars.com/kata/57de78848a8b8df8f10005b1/train/python

from typing import Union


def how_much_coffee(events: list[str]) -> Union[int, str]:
    counted_events = ("cw", "cat", "dog", "movie")
    coffee = 0
    for event in events:
        if event.lower() in counted_events:
            coffee += 2 if event.isupper() else 1
        if coffee > 3:
            return "You need extra sleep"
    return coffee


def test() -> None:
    print(how_much_coffee(['cw', 'CAT']))  # 3
    print(how_much_coffee(['cw', 'CAT', 'DOG']))  # You need extra sleep
    print(how_much_coffee(['cw', 'CAT', 'cw=others']))  # 3


if __name__ == "__main__":
    test()
