# https://www.codewars.com/kata/56cafdabc8cfcc3ad4000a2b/train/python

from time import sleep


def score(n: int) -> int:
    return (1 << n.bit_length()) - 1


def score_brute_force(n: int) -> int:
    output = 0
    for i in range(n + 1):
        output |= i
        print(f"i = {i} | n = {output}")
        sleep(0.25)
    return output


def test() -> None:
    test_cases = [0,  # 0
                  1,  # 1
                  49,  # 63
                  1_000_000  # 1 048 575
                  ]
    for test_case in test_cases:
        print(score(test_case))


if __name__ == "__main__":
    test()
