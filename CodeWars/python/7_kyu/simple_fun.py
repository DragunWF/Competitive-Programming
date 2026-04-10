# https://www.codewars.com/kata/5886f3713a111b620f0000dc/train/python

def html_end_tag_by_start_tag(start_tag: str) -> str:
    tag_name = start_tag.split(" ")[0][1:]
    if tag_name.endswith(">"):
        tag_name = tag_name[0:-1]
    return f"</{tag_name}>"


class TestCase:
    def __init__(self, start_tag: str, expected: str):
        self.start_tag = start_tag
        self.expected = expected


def test() -> None:
    test_cases = [
        TestCase("<button type='button' disabled>", "</button>"),
        TestCase("<i>", "</i>"),
        TestCase("<div id='my_area' class='data' title='This is a test for title on Div tag'>", "</div>")
    ]
    correct_count = 0
    for i, item in enumerate(test_cases):
        result = html_end_tag_by_start_tag(item.start_tag)
        is_correct = result == item.expected
        if is_correct:
            correct_count += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_correct else 'Failed'}")
        print(f"Input: {item.start_tag}")
        print(f"Result: {result}")
        print(f"Expected: {item.expected}\n")
    print(f"Test Cases Passed: {correct_count}/{len(test_cases)}")


if __name__ == "__main__":
    test()
