# https://www.codewars.com/kata/590f5b4a7bbb3e246000007d/train/python

def comes_after(s: str, l: str) -> str:
    output = ""
    l = l.lower()
    for i, char in enumerate(s):
        if char.lower() == l and i + 1 != len(s) and s[i + 1].isalpha():
            output += s[i + 1]
    return output


def test() -> None:
    print(comes_after("are you really learning Ruby?", "r"))  # eenu


if __name__ == "__main__":
    test()
