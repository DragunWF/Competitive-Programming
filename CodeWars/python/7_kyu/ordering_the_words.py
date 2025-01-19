# https://www.codewars.com/kata/55d7e5aa7b619a86ed000070/train/python

def order_word(s: str) -> str:
    if not s:
        return "Invalid String!"
    return "".join(sorted(s, key=ord))


def test() -> None:
    print(order_word("hello world!"))


if __name__ == "__main__":
    test()