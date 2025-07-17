# https://www.codewars.com/kata/5b1d1812b6989d61bd00004f/train/python

def find_nth_occurrence(substring: str, string: str, occurrence: int = 1) -> int:
    nth_occurence = 0
    for i in range(len(string)):
        if string[i:].startswith(substring):
            nth_occurence += 1
            if nth_occurence == occurrence:
                return i
    return -1


def test() -> None:
    string = "This is an example. Return the nth occurrence of example in this example string."
    print(find_nth_occurrence("example", string, 1))  # 11


if __name__ == "__main__":
    test()
