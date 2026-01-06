# https://www.codewars.com/kata/569924899aa8541eb200003f/train/python

def quicksum(packet: str) -> int:
    output = 0
    for i, char in enumerate(packet):
        is_uppercase_letter = char.isalpha() and char.isupper()
        if char != " " and not is_uppercase_letter:
            return 0
        if not is_uppercase_letter:
            continue
        output += (i + 1) * (ord(char) - 64)
    return output


def test() -> None:
    print(quicksum("ACM"))  # 46
    print(quicksum("A C M"))  # 75
    print(quicksum("AbqTH"))  # 0


if __name__ == "__main__":
    test()
