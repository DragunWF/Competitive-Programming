# https://www.codewars.com/kata/62fd5b557d267aa2d746bc19/train/python

from typing import Union


def matching(arg: list[str]) -> Union[int, float, str, None]:
    match arg:
        case []:
            return 0
        case [item]:
            if isinstance(item, int):
                return item
            return int(item) if item.isdigit() else item
        case [first, *_, last]:
            try:
                return int(first) / int(last)
            except (ZeroDivisionError, ValueError):
                return None
        case _:
            return None


def matching_old(arg: list[str]) -> Union[int, float, None]:
    if not type(arg) is list:
        return None
    if not arg:
        return 0
    if len(arg) == 1:
        if not type(arg[0]) is int:
            return int(arg[0]) if arg[0].isdigit() else arg[0]
        return arg[0]
    try:
        first_element = int(arg[0])
        last_element = int(arg[-1])
        return first_element / last_element
    except ZeroDivisionError:
        return None


def test() -> None:
    print(matching(''))  # --> None
    print(matching([]))  # --> 0
    print(matching(['2']))  # --> 2
    print(matching([0]))  # --> 0
    print(matching([3, 1, '2']))  # --> 1.5
    print(matching('123'))  # --> None
    print(matching(['0', 0]))  # --> None
    print(matching(['0', 2, '3']))  # --> 0.0


if __name__ == "__main__":
    test()
