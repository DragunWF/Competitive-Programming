# https://www.codewars.com/kata/5a2c22271f7f709eaa0005d3/train/python

def solve(s: str) -> str:
    if s == s[::-1]:
        return "OK"
    for i in range(len(s)):
        removed_one = s[:i] + s[i + 1:]
        if removed_one == removed_one[::-1]:
            return "remove one"
    return "not possible"


def test() -> None:
    print(solve("abba"))  # "OK"
    print(solve("abbaa"))  # "remove one"
    print(solve("abbaab"))  # "not possible"

    a = "aabaa"
    print(a[:2] + a[3:])


if __name__ == "__main__":
    test()
