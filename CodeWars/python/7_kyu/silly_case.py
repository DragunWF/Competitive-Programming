# https://www.codewars.com/kata/552ab0a4db0236ff1a00017a/train/python

def sillycase(silly: str) -> str:
    half = (len(silly) / 2).__ceil__()
    return f"{silly[0:half].lower()}{silly[half:].upper()}"


def test() -> None:
    print(sillycase("foobar"))
    print(sillycase("CODEWARS"))
    print(sillycase("brian"))
    print(sillycase("aa"))


if __name__ == "__main__":
    test()
