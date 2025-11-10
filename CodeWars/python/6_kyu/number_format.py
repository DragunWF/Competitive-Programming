# https://www.codewars.com/kata/565c4e1303a0a006d7000127/train/python

def number_format(n: int) -> str:
    if -999 <= n <= 999:
        return str(n)

    is_negative = n < 0
    str_num = str(abs(n))[::-1]
    formatted_number = []
    for i in range(len(str_num) - 1, -1, -1):
        formatted_number += str_num[i]
        if i % 3 == 0 and i != 0:
            formatted_number += ","

    formatted_number = "".join(formatted_number)
    if is_negative:
        return f"-{formatted_number}"
    return formatted_number


def test() -> None:
    print(number_format(100000))  # 100,000
    print(number_format(5678545))  # 5,678,545
    print(number_format(-420902))  # -420,902


if __name__ == "__main__":
    test()
