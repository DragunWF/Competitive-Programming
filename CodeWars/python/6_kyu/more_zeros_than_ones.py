# https://www.codewars.com/kata/5d41e16d8bad42002208fe1a/train/python

def more_zeros(s: str) -> list[str]:
    output = []
    for char in remove_duplicates(s):
        if is_more_zeros(bin(ord(char))[2:]):
            output.append(char)
    return output


def is_more_zeros(bin_num: str):
    return bin_num.count("0") > bin_num.count("1")


def remove_duplicates(s: str) -> str:
    uniques = ""
    for char in s:
        if not char in uniques:
            uniques += char
    return uniques


def test():
    # Not part of the solution, just testing
    # ['h', 'b', 'p', 'a', 'd']
    print(more_zeros('thequickbrownfoxjumpsoverthelazydog'))

    # ['T', 'H', 'E', 'Q', 'I', 'C', 'B', 'R', 'F', 'X', 'J', 'P', 'L', 'A', 'D']
    print(more_zeros('THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG'))

    # ['a', 'b', 'd', 'h', 'p', 'A', 'B', 'C', 'D', 'E', 'F', 'H', 'I', 'J', 'L', 'P', 'Q', 'R', 'T', 'X', '0']
    print(more_zeros('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_'))


if __name__ == "__main__":
    test()
