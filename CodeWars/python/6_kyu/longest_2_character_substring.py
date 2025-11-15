# https://www.codewars.com/kata/55bc0c54147a98798f00003e/train/python

from collections import defaultdict


def substring(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""

    char_counts = defaultdict(int)
    max_length = 0
    start_index = 0
    left = 0

    for right in range(n):
        char_counts[s[right]] += 1

        while len(char_counts) > 2:
            char_left = s[left]
            char_counts[char_left] -= 1

            if char_counts[char_left] == 0:
                del char_counts[char_left]

            left += 1

        current_length = right - left + 1
        if current_length > max_length:
            max_length = current_length
            start_index = left

    return s[start_index: start_index + max_length]


def substring_brute_force(s: str) -> str:
    longest_substring = ""
    for i in range(len(s)):
        for j in range(len(s)):
            substring = s[i:j + 1]
            unique_count = len(set(substring))
            if unique_count <= 2 and len(substring) > len(longest_substring):
                longest_substring = substring
            elif unique_count > 3:
                break
    return longest_substring


def test() -> None:
    print(substring("a"))  # => "a"
    print(substring("aaa"))  # => "aaa"
    print(substring("abacd"))  # => "aba"
    print(substring("abacddcd"))  # => "cddcd"
    print(substring("cefageaacceaccacca"))  # => "accacca"


if __name__ == "__main__":
    test()
