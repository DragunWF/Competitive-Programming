# https://www.codewars.com/kata/5441310626bc6a1e61000f2c/train/python


def colorful(number: int) -> bool:
    str_num = str(number)
    seen = set()
    for i in range(len(str_num)):
        current_product = int(str_num[i])
        if current_product in seen:
            return False
        seen.add(current_product)
        for j in range(i + 1, len(str_num)):
            current_product *= int(str_num[j])
            if current_product in seen:
                return False
            seen.add(current_product)
    return True


def test() -> None:
    print(colorful(263))  # True
    print(colorful(236))  # False


if __name__ == "__main__":
    test()
