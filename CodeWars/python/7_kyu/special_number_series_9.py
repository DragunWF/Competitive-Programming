# https://www.codewars.com/kata/58880c6e79a0a3e459000004

def tidyNumber(n: int) -> int:
    if n <= 9:
        return True
    str_num = str(n)
    for i in range(1, len(str_num)):
        if int(str_num[i]) < int(str_num[i - 1]):
            return False
    return True


def test() -> None:
    print(tidyNumber(12))  # True


if __name__ == "__main__":
    test()
