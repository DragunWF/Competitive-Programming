# https://www.codewars.com/kata/57eba158e8ca2c8aba0002a0/train/python

def last(s: str) -> str:
    words = s.split(" ")
    words.sort(key=lambda word: word[-1])
    return words


def test() -> None:
    print(last("man i need a taxi up to ubud"))


if __name__ == "__main__":
    test()
