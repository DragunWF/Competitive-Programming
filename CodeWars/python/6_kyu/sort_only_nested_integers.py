# https://www.codewars.com/kata/5a4bdd73d8e145f17d000035/train/python

def sort_nested_list(data: list) -> list:
    def flatten(item):
        for el in item:
            yield from flatten(el) if isinstance(el, list) else (el,)

    values = iter(sorted(flatten(data)))

    def reconstruct(item):
        return [reconstruct(el) if isinstance(el, list) else next(values) for el in item]

    return reconstruct(data)


def sort_nested_list_old(data: list) -> list:
    def helper(item) -> None:
        for element in item:
            if type(element) == list:
                if len(element) >= 2 and type(element[0]) == int:
                    element.sort()
                else:
                    helper(element)
    helper(data)
    return data


class TestCase:
    def __init__(self, data: list, expected: list) -> None:
        self.data = data
        self.expected = expected


def test() -> None:
    test_cases = [
        TestCase([[[]]], [[[]]]),
        TestCase([[[3, 2, 1]]], [[[1, 2, 3]]]),
        TestCase(
            [[[2, 1], [4, 3]], [[6, 5], [8, 7]]],
            [[[1, 2], [3, 4]], [[5, 6], [7, 8]]],
        ),
        TestCase([[[15, 30, 92]]], [[[15, 30, 92]]]),
        TestCase(
            [[[82, 87], [47, 44]], [[70, 94], [40, 64]]],
            [[[40, 44], [47, 64]], [[70, 82], [87, 94]]],
        ),
        TestCase(
            [[[29, 32], [82, 61], [75, 91]], [[69, 99], [74, 23], [70, 97]]],
            [[[23, 29], [32, 61], [69, 70]], [[74, 75], [82, 91], [97, 99]]],
        ),
    ]
    correct_count = 0
    for i, item in enumerate(test_cases):
        result = sort_nested_list(item.data)
        is_correct = result == item.expected
        if is_correct:
            correct_count += 1
        print(f"\nTest Case #{i + 1}: {'Pass' if is_correct else 'Fail'}")
        print(f"Input: {item.data}")
        print(f"Actual: {result}")
        print(f"Expected: {item.expected}\n")
    print(f"Test Cases Passed: {correct_count}/{len(test_cases)}")


if __name__ == "__main__":
    test()