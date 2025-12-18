# https://www.codewars.com/kata/5a7f58c00025e917f30000f1/train/python

def longest(s: str) -> int:  
    longest_substr = s[0]
    current_substr = longest_substr
    prev_char_ord = ord(s[0])
    for i in range(1, len(s)):
        current_char = s[i]
        current_char_ord = ord(s[i])
        if current_char_ord >= prev_char_ord:
            current_substr += current_char
            if len(current_substr) > len(longest_substr):
                longest_substr = current_substr
        else:
            current_substr = current_char
        prev_char_ord = current_char_ord
    return longest_substr


def test() -> None:
    # aaaabbbbctt
    print(longest("asdfaaaabbbbcttavvfffffdf"))


if __name__ == "__main__":
    test()