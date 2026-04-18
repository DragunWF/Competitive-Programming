# https://www.codewars.com/kata/699583ba5ca289725b496ad4/train/python

def broke_count(expenditures: list[int]) -> int:
    count = 0
    i = 0
    taken = []
    while i < len(expenditures):
        end = i + 7
        if end <= len(expenditures) and all([money <= 10 for money in expenditures[i:end]]):
            print([money <= 10 for money in expenditures[i:end]])
            taken.append(expenditures[i:end])
            count += 1
            i = end
        elif i + 3 <= len(expenditures) and all([money <= 7 for money in expenditures[i:i + 3]]):
            end = i + 3
            taken.append(expenditures[i:end])
            count += 1
            i = end
        elif expenditures[i] <= 3:
            count += 1
            i += 1
        else:
            i += 1
    return count


class TestCase:
    def __init__(self, expenditures: list[int], expected: int):
        self.expenditures = expenditures
        self.expected = expected


def test() -> None:
    test_cases: list[TestCase] = [
        TestCase([2], 1),                               # Single day <=3
        TestCase([5], 0),                               # Single day >3
        TestCase([5, 6, 7], 1),                         # Simple 3-day <=7
        TestCase([5, 6, 8], 0),                         # 3-day but interrupted
        TestCase([9, 8, 10, 9, 7, 6, 5], 1),            # Simple 7-day <=10
        TestCase([9, 8, 10, 12, 7, 6, 5], 1),           # 7-day interrupted but valid 3-day at end
        TestCase([2, 5, 6, 9, 8, 7, 6], 1),             # Overlap 3 inside 7 rule
        TestCase([2, 20, 2], 2),                        # Multiple independent <=3 days
        TestCase([5, 6, 7, 20, 5, 6, 7], 2),            # Multiple streaks separated
        TestCase([], 0)                                 # Empty list
    ]
    correct_count = 0
    for i, item in enumerate(test_cases):
        result = broke_count(item.expenditures)
        is_correct = result == item.expected
        if is_correct:
            correct_count += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_correct else 'Failed'}")
        print(f"Input: {item.expenditures}")
        print(f"Result: {result}")
        print(f"Expected: {item.expected}\n")
    print(f"Test Cases Passed: {correct_count}/{len(test_cases)}")


if __name__ == "__main__":
    print()
    test()
    print()
