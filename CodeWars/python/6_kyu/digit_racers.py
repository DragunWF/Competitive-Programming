# https://www.codewars.com/kata/682d3da198976a1e4c728d3c/train/python

from collections import Counter
from string import digits


def digit_racers(s: str) -> str:
    counter = Counter(s)
    placements: list[list[int]] = []
    last_count = None
    for key in sorted(counter, key=counter.get, reverse=True):
        count = counter[key]
        if count != last_count:
            placements.append([key])
        else:
            placements[-1].append(key)
        last_count = count

    for placement in placements:
        placement.sort(key=lambda digit: get_last_index(
            s, digit), reverse=True)

    return format_placements(placements)


def get_last_index(s: str, digit: str) -> int:
    for i in range(len(s) - 1, 0, -1):
        if s[i] == digit:
            return i
    return 0


def format_placements(placements: list[list[int]]) -> str:
    output = []
    seen_digits = set()
    for i, placement in enumerate(placements):
        ordinal = None
        placement_count = i + 1
        if placement_count == 1:
            ordinal = "st"
        elif placement_count == 2:
            ordinal = "nd"
        elif placement_count == 3:
            ordinal = "rd"
        else:
            ordinal = "th"
        output.append(
            f"{placement_count}{ordinal} place: {', '.join(placement)}")

        for digit in placement:
            seen_digits.add(digit)

    absent_digits = get_absent_digits(seen_digits)
    output.append(
        f"Absent digits: {', '.join(absent_digits)}" if absent_digits else "All digits present"
    )

    return "\n".join(output)


def get_absent_digits(seen_digits: set) -> list:
    absent_digits = []
    for digit in digits:
        if not digit in seen_digits:
            absent_digits.append(digit)
    return absent_digits


def test() -> None:
    print(digit_racers("00009393936611528"))
    print(digit_racers("5501234567789"))


if __name__ == "__main__":
    test()
