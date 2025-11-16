# https://www.codewars.com/kata/5f6d533e1475f30001e47514/train/python

def consecutive(arr: list[int], a: int, b: int) -> int:
    for i in range(len(arr) - 1):
        if (a == arr[i] and b == arr[i + 1]) or (a == arr[i + 1] and b == arr[i]):
            return True
    return False


def test() -> None:
    print(consecutive([1, 3, 5, 7], 3, 1))  # True


if __name__ == "__main__":
    test()
