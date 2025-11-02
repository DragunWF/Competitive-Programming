# https://www.codewars.com/kata/josephus-survivor

def josephus_survivor(n: int, k: int) -> int:
    winner = 0
    for i in range(2, n + 1):
        winner = (winner + k) % i
    return winner + 1


def test() -> None:
    # Expected: 4
    print(josephus_survivor(7, 3))


if __name__ == "__main__":
    test()
