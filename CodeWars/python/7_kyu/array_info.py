# https://www.codewars.com/kata/57f12b4d5f2f22651c00256d/train/python

def array_info(arr: list) -> list:
    N = len(arr)
    if not N:
        return "Nothing in the array!"

    integer_count = 0
    float_count = 0
    string_char_count = 0
    whitespace_count = 0
    for item in arr:
        if item == " ":
            whitespace_count += 1
        elif type(item) is int:
            integer_count += 1
        elif type(item) is float:
            float_count += 1
        elif type(item) is str:
            string_char_count += 1
    return [
        [N if N else None],
        [integer_count if integer_count else None],
        [float_count if float_count else None],
        [string_char_count if string_char_count else None],
        [whitespace_count if whitespace_count else None]
    ]


def test() -> None:
    # Expected: [[8],[3],[2],[2],[1]]
    print(array_info([1, 2, 3.33, 4, 5.01, 'bass', 'kick', ' ']))


if __name__ == "__main__":
    test()
