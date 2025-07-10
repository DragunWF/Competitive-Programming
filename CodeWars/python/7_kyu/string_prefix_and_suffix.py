# https://www.codewars.com/kata/5ce969ab07d4b7002dcaa7a1/train/python

def solve(s: str) -> int:
    prefixes = set()
    current_prefix = ""
    for i in range(len(s) // 2):
        current_prefix += s[i]
        prefixes.add(current_prefix)

    suffixes = set()
    current_suffix = ""
    for i in range(len(s) - 1, len(s) // 2 - 1, -1):
        current_suffix += s[i]
        suffixes.add(current_suffix[::-1])

    common_substrings = suffixes & prefixes
    if not common_substrings:
        return 0
    return max([len(item) for item in common_substrings])


def test() -> None:
    print(solve("abcd"))  # 0
    print(solve("abcabca"))  # 1 (Does not overlap)
    print(solve("abcdabc"))  # 3
    print(solve("abcabc"))  # 3


if __name__ == "__main__":
    test()
