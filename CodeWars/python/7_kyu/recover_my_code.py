# https://www.codewars.com/kata/69d3d8eac800a4e71c7e378d/train/python

from typing import Sequence


def restore_code(tokens: Sequence[Sequence[str]]) -> list[str]:
    commands = []
    variables = []
    for token in tokens:
        command = token[0]
        if not token[1].isalpha():
            continue
        if not is_int(token[2]) and not token[2].isalpha():
            continue

        if command == "set":
            variables.append(token[1])
            commands.append(f"{token[1]}={token[2]}")
        elif command == "add":
            commands.append(f"{token[1]}+={token[2]}")
        elif command == "sub":
            commands.append(f"{token[1]}-={token[2]}")
    return "\n".join(commands)


def is_int(num_str: str) -> bool:
    if not num_str:
        return False
    for char in num_str:
        if not char.isdigit() and char != "-":
            return False
    return True


class TestCase:
    def __init__(self, tokens: Sequence[Sequence[str]], expected: str):
        self.tokens = tokens
        self.expected = expected


def test() -> None:
    test_cases: list[TestCase] = [
        TestCase([
            ["set", "x", "3"],
            ["add", "x", "4"],
            ["set", "y", "2"],
            ["sub", "x", "y"],
        ], "x=3\nx+=4\ny=2\nx-=y"),

        TestCase([
            ["set", "a", "3"],
            ["noop", "a", "4"],
            ["set", "b", "6"],
            ["add", "a", "b"],
        ], "a=3\nb=6\na+=b"),

        TestCase([
            ["set", "total", "-12"],
            ["add", "answer", "total"],
            ["sub", "answer", "7"],
        ], "total=-12\nanswer+=total\nanswer-=7"),

        TestCase([
            ["mul", "x", "3"],
            ["set", "x1", "4"],
            ["sub", "y", "1.5"],
        ], ""),

        TestCase([], "")
    ]

    correct_count = 0
    for i, item in enumerate(test_cases):
        try:
            raw_result = restore_code(item.tokens)

            # The Codewars tests apply normalization for the valid cases
            # and strictly check for an empty string on the invalid/empty ones.
            if item.expected != "":
                result = normalize_source(raw_result)
            else:
                result = raw_result

            is_correct = result == item.expected
        except Exception as e:
            result = f"Error: {e}"
            is_correct = False

        if is_correct:
            correct_count += 1

        print(f"Test Case #{i + 1}: {'Passed' if is_correct else 'Failed'}")
        print(f"Input: {item.tokens}")
        # Using repr() to clearly visualize newlines and empty strings
        print(f"Result:   {repr(result)}")
        print(f"Expected: {repr(item.expected)}\n")

    print(f"Test Cases Passed: {correct_count}/{len(test_cases)}")


def normalize_source(source: str) -> str:
    if not source:
        return ""

    normalized_lines = []
    for line in source.split("\n"):
        compact = "".join(line.split())
        if compact:
            normalized_lines.append(compact)
    return "\n".join(normalized_lines)


if __name__ == "__main__":
    print()
    test()
    print()
