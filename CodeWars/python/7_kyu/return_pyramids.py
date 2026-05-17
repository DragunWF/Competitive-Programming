# https://www.codewars.com/kata/5a1c28f9c9fc0ef2e900013b

def pyramid(n: int) -> str:
    lines = []
    for i in range(n):
        filler_char = " " if i != n - 1 else "-"
        mid_fill = (i * 2) * filler_char
        start_fill = (n - (i + 1)) * " "
        lines.append(f"{start_fill}/{mid_fill}\\")
    return "\n".join(lines) + "\n"


class TestCase:
    def __init__(self, n: int, expected: str):
        self.n = n
        self.expected = expected


def test() -> None:
    test_cases = [
        TestCase(4, "   /\\\n  /  \\\n /    \\\n/______\\\n"),
        TestCase(6, "     /\\\n    /  \\\n   /    \\\n  /      \\\n /        \\\n/__________\\\n"),
        TestCase(10, "         /\\\n        /  \\\n       /    \\\n      /      \\\n     /        \\\n    /          \\\n   /            \\\n  /              \\\n /                \\\n/__________________\\\n")
    ]
    correct_count = 0
    for i, item in enumerate(test_cases):
        result = pyramid(item.n)
        is_correct = result == item.expected
        if is_correct:
            correct_count += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_correct else 'Failed'}")
        print(f"Input: {item.n}")
        print(f"Result: {result}")
        print(f"Expected: {item.expected}\n")
    print(f"Test Cases Passed: {correct_count}/{len(test_cases)}")


if __name__ == "__main__":
    print()
    test()
    print()

# '   /\\\n  /  \\\n /    \\\n/------\\\n' 
# '   /\\\n  /  \\\n /    \\\n/______\\\n'