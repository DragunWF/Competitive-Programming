# https://www.codewars.com/kata/597a660f59873cc353000061

def get_colors(col_arr: list[str]) -> str:
    combinations = []
    for colors in col_arr:
        dominant_color_count = {
            "Red": 0,
            "Green": 0,
            "Blue": 0
        }
        for hexadecimal in colors:
            color_values = {
                int(hexadecimal[:2], 16): "Red",
                int(hexadecimal[2:4], 16): "Green",
                int(hexadecimal[4:6], 16): "Blue"
            }

            max_color_value = max(color_values.keys())
            dominant_color = color_values[max_color_value]
            dominant_color_count[dominant_color] += 1

        rgb_values = list(dominant_color_count.values())
        rgb_values.sort(reverse=True)

        value_to_color_map = invert_dict(dominant_color_count)
        major_color = value_to_color_map[rgb_values[0]]
        minor_color = value_to_color_map[rgb_values[1]]
        combinations.append(f"{major_color}+{minor_color}")
    return ",".join(combinations)


def invert_dict(map: dict) -> dict:
    output = {}
    for key in map:
        output[map[key]] = key
    return output


class TestCase:
    def __init__(self, col_arr: list[str], expected: str):
        self.col_arr = col_arr
        self.expected = expected


def test() -> None:
    test_cases: list[TestCase] = [
        TestCase([["6B8E23", "9ACD32", "2E8B57", "00008B", "00FF00", "6B8E23", "00FA9A"],
                  ["CD5C5C", "8B0000", "FF0000", "F08080", "98FB98", "DC143C"],
                  ["00BFFF", "00008B", "B22222", "000080", "87CEEB", "4169E1"]], "Green+Blue,Red+Green,Blue+Red"),
        TestCase([["FF0000", "191970", "FF0000"],
                  ["556B2F", "98FB98", "2E8B57", "00FF7F", "556B2F", "FFA07A"],
                  ["00BFFF", "00BFFF", "4169E1", "1E90FF", "F08080", "191970"]], "Red+Blue,Green+Red,Blue+Red"),
        TestCase([["FF0000", "8DC4DE", "87CEFA", "4169E1", "0000FF"],
                  ["FF0000", "191970", "00008B"],
                  ["CD5C5C", "F08080", "0000FF"]], "Blue+Red,Blue+Red,Red+Blue")
    ]
    correct_count = 0
    for i, item in enumerate(test_cases):
        result = get_colors(item.col_arr)
        is_correct = result == item.expected
        if is_correct:
            correct_count += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_correct else 'Failed'}")
        print(f"Input: {item.col_arr}")
        print(f"Result: {result}")
        print(f"Expected: {item.expected}\n")

    percentage_passed = round((correct_count / len(test_cases)) * 100)
    print(f"Test Cases Passed: {correct_count}/{len(test_cases)} - {percentage_passed}%")


if __name__ == "__main__":
    print()
    test()
    print()
