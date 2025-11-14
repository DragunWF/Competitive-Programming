# https://www.codewars.com/kata/5546180ca783b6d2d5000062


def squares(x: int, n: int) -> list[int]:
    if n <= 0:
        return []

    output = [x]
    current_num = x
    for i in range(n - 1):
        current_num = current_num ** 2
        output.append(current_num)
    return output


def test() -> None:
    # Expected: [2, 4, 16, 256, 65536]
    print(squares(2, 5))
    # Expected: [3, 9, 81]
    print(squares(3, 3))


if __name__ == "__main__":
    test()
