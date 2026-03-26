# https://www.codewars.com/kata/586e1d458cb711f0a800033b/train/python

def process_data(data: list[list[int]]) -> int:
    result = None
    for pair in data:
        difference = pair[0] - pair[1]
        if result is None:
            result = difference
        else:
            result *= difference
    return result


def test() -> None:
    # 3
    print(process_data([[2, 5], [3, 4], [8, 7]]))

    # 28
    print(process_data([[2, 9], [2, 4], [7, 5]]))


if __name__ == "__main__":
    test()
