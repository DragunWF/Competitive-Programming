# https://www.codewars.com/kata/56a4872cbb65f3a610000026/train/python

def max_rot(n: int) -> int:
    rotations = []
    digits = [*str(n)]
    for i in range(len(digits)):
        rotations.append(int("".join(digits)))
        for j in range(i, len(digits) - 1):
            digits[j], digits[j + 1] = digits[j + 1], digits[j]
    return max(rotations)


def test() -> None:
    print(max_rot(56789))  # 68957
    print(max_rot(38458215))  # 85821534


if __name__ == "__main__":
    test()
