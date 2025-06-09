# https://www.codewars.com/kata/57193a349906afdf67000f50/train/python

def magic_sum(arr: list[int]) -> int:
    total_magic_sum = 0
    for number in arr:
        str_num = str(number)
        if number % 2 != 0 and "3" in str_num:
            total_magic_sum += number
    return total_magic_sum


def test() -> None:
    print(magic_sum([3, 12, 5, 8, 30, 13]))  # 16 (3 + 13)


if __name__ == "__main__":
    test()
