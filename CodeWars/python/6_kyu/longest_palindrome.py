# https://www.codewars.com/kata/54bb6f887e5a80180900046b/train/python

def longest_palindrome(s: str) -> str:
    if not s or len(s) == 1:
        return len(s)

    end_pointer = len(s) - 1
    palindrome_lengths = []
    while end_pointer > 0:
        for pointer in range(end_pointer + 1):
            substring = s[pointer:end_pointer + 1]
            is_palindrome = substring == substring[::-1]
            if is_palindrome:
                palindrome_lengths.append(len(substring.strip()))
        end_pointer -= 1
    return max(palindrome_lengths)


def test() -> None:
    print(longest_palindrome("a"))  # 1
    print(longest_palindrome("aab"))  # 2
    print(longest_palindrome("abcde"))  # 1
    print(longest_palindrome("zzbaabcd"))  # 4
    print(longest_palindrome(""))  # 0
    print(longest_palindrome("baablkj12345432133d"))  # 9


if __name__ == "__main__":
    test()
