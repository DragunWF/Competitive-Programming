# https://www.codewars.com/kata/55cb000321ca31039e00007d/train/python

def geometric_sequence_sum(a: int, r: int, n: int) -> int:
    current_term = a
    sequence_sum = current_term
    for i in range(n - 1):
        current_term *= r
        sequence_sum += current_term
    return sequence_sum


def test() -> None:
    print(geometric_sequence_sum(2, 3, 5))  # 242


if __name__ == "__main__":
    test()
