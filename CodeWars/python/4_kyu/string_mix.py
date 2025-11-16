# https://www.codewars.com/kata/5629db57620258aa9d000014

from collections import Counter


def mix(s1: str, s2: str) -> str:
    s1_counter = Counter(filter_for_lowercase_char(s1))
    s2_counter = Counter(filter_for_lowercase_char(s2))
    common = filter_for_multiple_counts(s1_counter, s2_counter)
    diff = []
    for char in common:
        prefix = None
        count = max(s1_counter[char], s2_counter[char])
        if s1_counter[char] > s2_counter[char]:
            prefix = "1"
        elif s1_counter[char] < s2_counter[char]:
            prefix = "2"
        else:
            prefix = "="
        diff.append(f"{prefix}:{char * count}")
    diff.sort(key=lambda item: (-len(item[2:]), item))
    return "/".join(diff)


def filter_for_lowercase_char(s: str) -> list:
    return [char for char in s if char.isalpha() and char.islower()]


def filter_for_multiple_counts(s1_counter: Counter, s2_counter: Counter) -> list:
    common = set(s1_counter.keys()) | set(s2_counter.keys())
    output = []
    for char in common:
        if s1_counter[char] > 1 or s2_counter[char] > 1:
            output.append(char)
    return output


def test() -> None:
    # Expected: 1:aaaa/2:bbb
    print(mix("A aaaa bb c", "& aaa bbb c d"))

    # Expected: "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"
    print(mix("Are the kids at home? aaaaa fffff",
          "Yes they are here! aaaaa fffff"))


if __name__ == "__main__":
    test()
