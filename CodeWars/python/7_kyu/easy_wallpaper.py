# https://www.codewars.com/kata/567501aec64b81e252000003

numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
           "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]


from math import ceil


def wallpaper(l: float, w: float, h: float) -> str:
    if not l or not w or not h:
        return "zero"
    wall_area = (2 * l * h) + (2 * w * h)
    roll_area = 0.52 * 10
    return numbers[ceil((wall_area / roll_area) * 1.15)]


class TestCase:
    def __init__(self, l: float, w: float, h: float, expected: str):
        self.l = l
        self.w = w
        self.h = h
        self.expected = expected


def test() -> None:
    test_cases = [
        TestCase(6.3, 4.5, 3.29, "sixteen"),
        TestCase(7.8, 2.9, 3.29, "sixteen"),
        TestCase(6.3, 5.8, 3.13, "seventeen"),
        TestCase(6.1, 6.7, 2.81, "sixteen"),
        TestCase(7.9, 5.4, 0, "zero"),
        TestCase(7.9, 0, 5.4, "zero")
    ]
    correct_count = 0
    for i, item in enumerate(test_cases):
        result = wallpaper(item.l, item.w, item.h)
        is_correct = result == item.expected
        if is_correct:
            correct_count += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_correct else 'Failed'}")
        print(f"Input: l = {item.l}, w = {item.w}, h = {item.h}")
        print(f"Result: {result}")
        print(f"Expected: {item.expected}\n")
    print(f"Test Cases Passed: {correct_count}/{len(test_cases)}")


if __name__ == "__main__":
    print()
    test()
    print()
