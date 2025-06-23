# https://www.codewars.com/kata/587e18b97a25e865530000d8/train/python

from collections import Counter


def anagram_counter(words: list) -> list:
    for i in range(len(words)):
        words[i] = "".join(sorted([*words[i]]))

    anagram_count = 0
    word_counter = Counter(words)
    for key in word_counter:
        count = word_counter[key]
        if count >= 2:
            anagram_count += count * (count - 1) // 2
    return anagram_count


def test() -> None:
    print(anagram_counter(["dell", "ledl", "abc", "cba"]))
    print(anagram_counter(["dell", "ledl", "abc", "cba", "bca", "bac"]))


if __name__ == "__main__":
    test()
