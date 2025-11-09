# https://www.codewars.com/kata/5259acb16021e9d8a60010af/train/python

def lcm(*args):
    """
    Compute the least common multiple of some non-negative integers
    """
    if not args:
        return 1
    if 0 in args:
        return 0

    nums = set(args)
    max_num = max(nums)
    i = 1
    while True:
        candidate = max_num * i
        for num in nums:
            if candidate % num != 0:
                break
        else:
            return candidate
        i += 1


def test() -> None:
    print(lcm(5, 6, 7, 9, 6, 9, 18, 4, 5, 15, 15, 10, 17, 7))  # 21420


if __name__ == "__main__":
    test()
