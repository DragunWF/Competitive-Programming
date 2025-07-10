# https://www.codewars.com/kata/5ce969ab07d4b7002dcaa7a1/train/python

class Substring:
    def __init__(self, content: str, start_index: int, end_index: int):
        self.content = content
        self.start_index = start_index
        self.end_index = end_index


def solve(s: str) -> int:
    prefixes = set()
    current_prefix = ""
    for char in s:
        current_prefix += char
        prefixes.add(current_prefix)

    suffixes = []
    current_suffix = ""
    print(prefixes)
    for i in range(len(s) - 1, 0, -1):
        current_suffix += s[i]
        reversed_suffix = current_suffix[::-1]
        print(reversed_suffix)
        if reversed_suffix in prefixes:
            suffixes.append(len(current_suffix[::-1]))
    return max(suffixes) if suffixes else 0


def test() -> None:
    print(solve("abcd"))  # 3
    print(solve("abcabca"))  # 1 (Does not overlap)


if __name__ == "__main__":
    test()
