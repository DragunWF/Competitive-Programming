# https://www.codewars.com/kata/51edd51599a189fe7f000015

def solution(array_a: list, array_b: list) -> int:
    N = len(array_a)
    total = 0
    for i in range(N):
        total += abs(array_a[i] - array_b[i]) ** 2
    return total / N


def test() -> None:
    print(solution([1, 2, 3], [4, 5, 6]))  # 9
    print(solution([10, 20, 10, 2], [10, 25, 5, -2]))  # 16.5
    print(solution([-1, 0], [0, -1]))  # 1


if __name__ == "__main__":
    test()
