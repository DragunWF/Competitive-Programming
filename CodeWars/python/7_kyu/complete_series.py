# https://www.codewars.com/kata/580a4001d6df740d61000301

def complete_series(seq: list[int]) -> list[int]:
    if len(seq) != len(set(seq)):
        return [0]
    output = []
    max_num = max(seq)
    for i in range(max_num + 1):
        output.append(i)
    return output


def test() -> None:
    print(complete_series([2, 1]))  # [0, 1, 2]
    print(complete_series([1, 4, 4, 6]))  # [0]


if __name__ == "__main__":
    test()
