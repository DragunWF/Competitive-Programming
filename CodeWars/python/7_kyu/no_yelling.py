# https://www.codewars.com/kata/587a75dbcaf9670c32000292

def filter_words(s: str) -> str:
    return " ".join([word for word in s.split(" ") if word]).capitalize()


def test() -> None:
    print(filter_words('This    will    not    pass '))


if __name__ == "__main__":
    test()
