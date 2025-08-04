# https://www.codewars.com/kata/5512e5662b34d88e44000060/train/python

def find_missing_number(sequence: str) -> int:
    if not sequence:
        return 0

    try:
        nums = sorted(int(n) for n in sequence.split(" "))
        if nums[0] != 1:
            return 1

        for i in range(1, len(nums)):
            current_num = nums[i]
            target_num = nums[i - 1] + 1
            if current_num != target_num:
                return target_num
        return 0
    except ValueError:
        return 1


def test() -> None:
    print(find_missing_number("1 2 4 3"))  # 0
    print(find_missing_number("1 a 4 3"))  # 1
    print(find_missing_number("1 2 4"))  # 3


if __name__ == "__main__":
    test()
