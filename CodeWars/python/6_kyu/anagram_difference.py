# https://www.codewars.com/kata/5b1b27c8f60e99a467000041/train/python

from collections import Counter


def anagram_difference(w1: str, w2: str) -> str:
    total = 0
    w1_counter = Counter(w1)
    w2_counter = Counter(w2)
    total += get_letter_difference(w1_counter, w2_counter)
    total += get_letter_difference(w2_counter, w1_counter)
    for key in w1_counter:
        if key in w2_counter:
            total += abs(w1_counter[key] - w2_counter[key])
    return total


def get_letter_difference(w1_counter: Counter, w2_counter: Counter) -> int:
    total = 0
    for key in w1_counter:
        if not key in w2_counter:
            total += w1_counter[key]
    return total


if __name__ == '__main__':
    # Test
    print(anagram_difference("codewars", "hackerrank"))  # 10
