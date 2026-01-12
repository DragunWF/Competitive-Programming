# https://www.codewars.com/kata/5effa412233ac3002a9e471d/train/python

def add(num1: int, num2: int) -> int:
    str_num1 = str(num1)[::-1]
    str_num2 = str(num2)[::-1]
    sums = []
    for i in range(max(len(str_num1), len(str_num2))):
        first_num = int(str_num1[i]) if i < len(str_num1) else 0
        second_num = int(str_num2[i]) if i < len(str_num2) else 0
        sums.append(str(first_num + second_num))
    sums.reverse()
    return int("".join(sums))


def test() -> None:
    # Expected: 214
    print(add(16, 18))


if __name__ == "__main__":
    test()
