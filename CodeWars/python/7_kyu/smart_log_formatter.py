# https://www.codewars.com/kata/6ab3da4db0d8c965cd93923e

def smart_log_formatter(logs: list[str]) -> list[str]:
    prev = None
    duplicate_count = 1
    output = []
    for log in logs:
        if prev == log:
            duplicate_count += 1
            if not output:
                output.append(log)
            output[-1] = f"{log} (x{duplicate_count})"
        else:
            output.append(log)
            duplicate_count = 1
        prev = log
    return output


class TestCase:
    def __init__(self, value: list[str], expected: list[str]):
        self.value = value
        self.expected = expected


def test():
    test_cases = [
        TestCase([
            "ERROR Disk failure",
            "ERROR Disk failure",
            "ERROR Disk failure",
            "INFO User login"
        ], [
            "ERROR Disk failure (x3)",
            "INFO User login"
        ]),
        TestCase([
            "INFO Connected",
            "WARNING Low battery",
            "INFO Connected"
        ],
            [
            "INFO Connected",
            "WARNING Low battery",
            "INFO Connected"
        ]
        )
    ]
    correct_count = 0
    for i, test_case in enumerate(test_cases):
        result = smart_log_formatter(test_case.value)
        is_correct = result == test_case.expected
        if is_correct:
            correct_count += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_correct else 'Failed'}")
        print(f"Input: {test_case.value}")
        print(f"Result: {result}")
        print(f"Expected: {test_case.expected}")
    print(f"Test Cases Passed: {correct_count}/{len(test_cases)}")


if __name__ == "__main__":
    test()

# Failed with logs:
# ['INFO login', 'INFO login', 'ERROR failed', 'ERROR failed', 'INFO login']:
# ['INFO login (x2)', 'ERROR failed (x3)', 'INFO login']
# should equal
# ['INFO login (x2)', 'ERROR failed (x2)', 'INFO login']
