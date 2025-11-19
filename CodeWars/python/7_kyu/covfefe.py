# https://www.codewars.com/kata/592fd8f752ee71ac7e00008a/train/python

def covfefe(s: str) -> str:
    substring_found = False
    while "coverage" in s:
        s = s.replace("coverage", "covfefe")
        substring_found = True
    if not substring_found:
        s += " covfefe"
    return s


def test() -> None:
    print(covfefe("coverage coverage"))
    print(covfefe("nothing"))


if __name__ == "__main__":
    test()
