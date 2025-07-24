# https://www.codewars.com/kata/5822d89270ca28c85c0000f3/train/python

def scramble(s: str, array: list[int]) -> str:
    output = [*(" " * len(array))]
    for i, position in enumerate(array):
        output[position] = s[i]
    return "".join(output)


def test() -> None:
    print(scramble("abcd", [0, 3, 1, 2]))  # 'acdb'


if __name__ == "__main__":
    test()
