# https://www.codewars.com/kata/56121f3312baa28c8500005b/train/python

def biggest(nums: list[int]) -> list[int]:
    return str(int("".join(sorted(map(str, nums), key=lambda x: x*10, reverse=True))))


def test() -> None:
    print(biggest([1, 2, 3]))  # "321" (3-2-1)
    print(biggest([3, 30, 34, 5, 9]))  # "9534330" (9-5-34-3-30)


if __name__ == "__main__":
    test()
