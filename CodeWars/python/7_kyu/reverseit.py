# https://www.codewars.com/kata/557a2c136b19113912000010/train/python

def reverse_it(data) -> str:
    if type(data) == str:
        return data[::-1]
    if type(data) == int:
        return int(str(data)[::-1])
    if type(data) == float:
        return float(str(data)[::-1])
    return data


def test() -> None:
    print(reverse_it("abcde"))


if __name__ == '__main__':
    test()
