# https://www.codewars.com/kata/56be4affc5dc03b84b001d2d/python

def get_reversed_color(hex_color: str) -> str:
    if not type(hex_color) is str or len(hex_color) > 6:
        raise Exception("Invalid hex value!")
    if len(hex_color) < 6:
        hex_color = pad_zeros(hex_color)
    hex_color = hex_color.upper()

    hex_chars = [*"0123456789ABCDEF"]
    decimal_map = create_decimal_map(hex_chars)
    output = []
    for char in hex_color:
        decimal = decimal_map[char]
        complement_index = len(hex_chars) - decimal - 1
        output.append(hex_chars[complement_index])
    return f"#{''.join(output)}"


def create_decimal_map(hex_chars: list[str]) -> dict[str, int]:
    decimal_map = {}
    for i, char in enumerate(hex_chars):
        decimal_map[char] = i
    return decimal_map


def pad_zeros(hex_color: str) -> str:
    REQUIRED = 6
    pad_count = REQUIRED - len(hex_color)
    return pad_count * '0' + hex_color


class TestCase:
    def __init__(self, hex_color: str, expected: str):
        self.hex_color = hex_color
        self.expected = expected


def test() -> None:
    test_cases = [
        TestCase("01fD08", "#FE02F7"),
        TestCase("a23", "#FFF5DC"),
        TestCase("", "#FFFFFF")
    ]
    correct_count = 0
    for i, item in enumerate(test_cases):
        result = get_reversed_color(item.hex_color)
        is_correct = result == item.expected
        if is_correct:
            correct_count += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_correct else 'Failed'}")
        print(f"Input: {item.hex_color}")
        print(f"Result: {result}")
        print(f"Expected: {item.expected}\n")
    print(f"Test Cases Passed: {correct_count}/{len(test_cases)}")


if __name__ == "__main__":
    test()
