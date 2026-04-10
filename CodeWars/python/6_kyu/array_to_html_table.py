# https://www.codewars.com/kata/5e7e4b7cd889f7001728fd4a

def to_table(data: list[list], header=False, index=False):
    table_rows = []
    full_table_header = ""
    for i, items in enumerate(data):
        if header and i == 0:
            table_header_data = []
            if index:
                table_header_data.append("<th></th>")
            for element in items:
                table_header_data.append(f"<th>{element}</th>")
            full_table_header = f"<thead><tr>{''.join(table_header_data)}</tr></thead>"
            continue

        table_row = []
        if index:
            table_row.append(f"<td>{i + 1 if not header else i}</td>")
        for element in items:
            table_row.append(f"<td>{element if not element is None else ''}</td>")
        table_rows.append(f"<tr>{''.join(table_row)}</tr>")
    return f"<table>{full_table_header}<tbody>{''.join(table_rows)}</tbody></table>"


class TestCase:
    def __init__(self, data: list[list], expected: str, header: bool = False, index: bool = False):
        self.data = data
        self.expected = expected
        self.header = header
        self.index = index


def test() -> None:
    test_cases = [
        TestCase(
            [["o"]],
            "<table><tbody><tr><td>o</td></tr></tbody></table>"
        ),
        TestCase(
            [["lorem", "ipsum"], ["dolor", "sit amet"]],
            "<table><thead><tr><th></th><th>lorem</th><th>ipsum</th></tr></thead><tbody><tr><td>1</td><td>dolor</td><td>sit amet</td></tr></tbody></table>",
            header=True,
            index=True
        ),
        TestCase(
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            "<table><tbody><tr><td>1</td><td>1</td><td>2</td><td>3</td></tr><tr><td>2</td><td>4</td><td>5</td><td>6</td></tr><tr><td>3</td><td>7</td><td>8</td><td>9</td></tr></tbody></table>",
            header=False,
            index=True
        ),
        TestCase(
            [
                ["id", "name", "price", "quantity"],
                [24351, "pen", 2.41, 500],
                [None, "pencil", 0.99, 25],
                [63401, "grizzly bear", None, 1],
                [3532, "rubber duck", 5.45, 24],
                [1523, None, 3.00, 6.8],
                [11765, "caviar", 67.95, None]
            ],
            "<table><thead><tr><th>id</th><th>name</th><th>price</th><th>quantity</th></tr></thead><tbody><tr><td>24351</td><td>pen</td><td>2.41</td><td>500</td></tr><tr><td></td><td>pencil</td><td>0.99</td><td>25</td></tr><tr><td>63401</td><td>grizzly bear</td><td></td><td>1</td></tr><tr><td>3532</td><td>rubber duck</td><td>5.45</td><td>24</td></tr><tr><td>1523</td><td></td><td>3.0</td><td>6.8</td></tr><tr><td>11765</td><td>caviar</td><td>67.95</td><td></td></tr></tbody></table>",
            header=True
        ),
        TestCase(
            [["a", "b", "c", "d", "e"], [True, False, False, True, True]],
            "<table><thead><tr><th>a</th><th>b</th><th>c</th><th>d</th><th>e</th></tr></thead><tbody><tr><td>True</td><td>False</td><td>False</td><td>True</td><td>True</td></tr></tbody></table>",
            header=True
        )
    ]
    correct_count = 0
    for i, item in enumerate(test_cases):
        result = to_table(item.data, item.header, item.index)
        is_correct = result == item.expected
        if is_correct:
            correct_count += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_correct else 'Failed'}")
        print(f"Input: data = {item.data}, header = {item.header}, index = {item.index}")
        print(f"Result: {result}")
        print(f"Expected: {item.expected}\n")
    print(f"Test Cases Passed: {correct_count}/{len(test_cases)}")


if __name__ == "__main__":
    print()
    test()
    print()
