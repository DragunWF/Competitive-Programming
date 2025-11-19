# https://www.codewars.com/kata/5a090c4e697598d0b9000004/train/python

def solve(arr: list[int]):
    current = [*arr]
    output = []
    is_max = True  # For alternating
    while current:
        selected = max(current) if is_max else min(current)
        output.append(current.pop(current.index(selected)))
        is_max = not is_max
    return output


def test() -> None:
    print(solve([15, 11, 10, 7, 12]))  # = [15,7,12,10,11]


if __name__ == "__main__":
    test()
