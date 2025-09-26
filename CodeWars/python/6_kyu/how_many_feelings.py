# https://www.codewars.com/kata/5a33ec23ee1aaebecf000130/train/python

from collections import Counter


def count_feelings(s: str, arr: list[str]) -> str:
    target_counter = Counter(s)
    feelings_count = 0
    for word in arr:
        word_counter = Counter(word)
        is_present = True
        for char in word_counter:
            if target_counter[char] < word_counter[char]:
                is_present = False
                break
        if is_present:
            feelings_count += 1
    return f"{feelings_count} {'feelings' if feelings_count != 1 else 'feeling'}."


def test() -> None:
    # Expected: 3 feelings
    print(count_feelings("yliausoenvjw", [
          'anger', 'awe', 'joy', 'love', 'grief']))


if __name__ == "__main__":
    test()
