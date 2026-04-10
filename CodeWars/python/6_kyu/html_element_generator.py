# https://www.codewars.com/kata/5e7837d0262211001ecf04d7/train/python

def html(*args: list, **kwargs: dict) -> str:
    tag = args[0]
    content = None
    if len(args) > 1:
        content = args[1:]

    attributes = []
    for keyword in kwargs:
        if keyword == "cls":
            attributes.append(f'class="{kwargs[keyword]}"')
            continue
        attributes.append(f'{keyword}="{kwargs[keyword]}"')
    attributes_str = " " + " ".join(attributes)
    if not attributes:
        attributes_str = attributes_str.lstrip()

    if content:
        full_tag = f"<{tag}{attributes_str}>"
        tags = []
        for item in content:
            tags.append(f"{full_tag}{item}</{tag}>")
        return "\n".join(tags)
    return f"<{tag}{attributes_str} />"


class TestCase:
    def __init__(self, expected: str, *args: list, **kwargs: dict):
        self.expected = expected
        self.args = args
        self.kwargs = kwargs


def test() -> None:
    test_cases = [
        TestCase('<img src="/images/img.png" />', 'img', src="/images/img.png"),
        TestCase('<br />', 'br'),
        TestCase('<p class="paragraph-text" id="example">Hello World!</p>\n<p class="paragraph-text" id="example">This is html code!</p>',
                 'p', 'Hello World!', 'This is html code!', cls="paragraph-text", id="example"),
        TestCase('<form method="post" action="somefile.php">Some text in here, too</form>',
                 'form', 'Some text in here, too', method='post', action='somefile.php'),
        TestCase('<input type="text" id="thisinput" name="InsertName" size="50" />',
                 'input', type='text', id="thisinput", name="InsertName", size="50"),
        TestCase('<span class="span1" style="color: red;" role="main">This text would be red</span>',
                 'span', 'This text would be red', cls="span1", style="color: red;", role="main"),
        TestCase('<title>Webpage Title</title>', 'title', 'Webpage Title'),
        TestCase('<ul class="list">This would be <li> elements.</ul>',
                 'ul', "This would be <li> elements.", cls="list"),
        TestCase('<table border="1 px solid gold">    </table>', "table", "    ", border="1 px solid gold"),
        TestCase('<h1 randomattributename="randomattributevalue">This is a header</h1>',
                 "h1", "This is a header", randomattributename="randomattributevalue")
    ]

    correct_count = 0
    for i, item in enumerate(test_cases):
        try:
            result = html(*item.args, **item.kwargs)
            is_correct = result == item.expected
        except Exception as e:
            result = f"Error: {e}"
            is_correct = False

        if is_correct:
            correct_count += 1

        print(f"Test Case #{i + 1}: {'Passed' if is_correct else 'Failed'}")
        print(f"Input: args = {item.args}, kwargs = {item.kwargs}")
        print(f"Result:   {repr(result)}")
        print(f"Expected: {repr(item.expected)}\n")

    print(f"Test Cases Passed: {correct_count}/{len(test_cases)}")


if __name__ == "__main__":
    print()
    test()
    print()
