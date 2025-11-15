# https://www.codewars.com/kata/59f7597716049833200001eb/train/python

def solve(a: int, b: int) -> int:
    count = 0
    for i in range(a, b):
        if is_same_rotated(i):
            count += 1
    return count


def is_same_rotated(n: int) -> bool:
    reversions = {"6": "9", "9": "6"}
    same_reversions = ["0", "1", "8"]
    str_num = str(n)
    reversed_str_num = str_num[::-1]
    output = ""
    for digit in reversed_str_num:
        if digit in reversions:
            output += reversions[digit]
        elif digit in same_reversions:
            output += digit
        else:
            return False
    return str_num == output


def test() -> None:
    print(solve(0, 10))  # 3
    print(solve(10, 100))  # 4
    print(solve(100, 1000))  # 12

    print(is_same_rotated(9116))  # True
    print(is_same_rotated(123))  # False
    print(is_same_rotated(6969))  # True


if __name__ == "__main__":
    test()
