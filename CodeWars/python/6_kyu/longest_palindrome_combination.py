# https://www.codewars.com/kata/5a0178f66f793bc5b0001728

from collections import Counter


def longest_palindrome(s: str) -> str:
    freq = Counter(char for char in s.lower() if char.isalnum())
    palindrome_length = 0
    odd_found = False
    for char in freq:
        if freq[char] % 2 == 0:
            palindrome_length += freq[char]
        else:
            odd_found = True
            palindrome_length += freq[char] - 1
    if odd_found:
        palindrome_length += 1
    return palindrome_length


def test() -> None:
    print(longest_palindrome("Hannah"))  # 6
    print(longest_palindrome("xyz__a_/b0110//a_zyx"))  # 13
    print(longest_palindrome("lol"))  # 3
    print(longest_palindrome("racecar"))  # 7
    print(longest_palindrome("AqR2eCo0?WlozlJ.Ggj3./!7WeP7IQ>B0Sr,h5GmFIZMi0kOHrSo*z-Gy>f9Y?fOR2eJjt.CL0Y4JKFaGVe<HwIKMzJu2ggo5XReE9bjU=5HqzAWLVL/FHgL,KwcaIF*9X3-YVulWE=ml4mow.eDqy0di-mBW*0,iM>i-mE6.?j0k/QFcbcdDBiM146LFj9A1Za5yl5>"))  # 153


if __name__ == "__main__":
    test()
