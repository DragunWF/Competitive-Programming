# https://www.codewars.com/kata/5800b6568f7ddad2c10000ae/train/python

def simplify(number: int) -> str:
    if not number:
        return ""
    factors = []
    str_num = str(number)
    digit_length = len(str_num)
    for i, digit in enumerate(str_num):
        if digit == "0":
            continue
        zero_count = digit_length - i - 1
        if zero_count <= 0:
            factors.append(digit)
            continue
        factors.append(f"{digit}*1{'0' * zero_count}")
    return "+".join(factors)


def test() -> None:
    print(simplify(0))  # -->  ""
    print(simplify(56))  # -->  "5*10+6"
    print(simplify(60))  # -->  "6*10"
    print(simplify(999))  # -->  "9*100+9*10+9"
    print(simplify(10004))  # -->  "1*10000+4"


if __name__ == "__main__":
    test()
