# https://www.codewars.com/kata/59f44c7bd4b36946fd000052/train/python

def hist(s: str) -> str:
    error_count = {"u": 0, "w": 0, "x": 0, "z": 0}
    for char in s:
        if char in error_count:
            error_count[char] += 1
    return convert_to_hist(error_count)


def convert_to_hist(error_count: dict) -> str:
    output = []
    for key in error_count:
        if error_count[key] > 0:
            whitespace_count = 5 if error_count[key] <= 9 else 4
            output.append(
                f"{key}{' ' * 2}{error_count[key]}{' ' * whitespace_count}{'*' * error_count[key]}"
            )
    return "\r".join(output)


def test() -> None:
    # Expected: "u  2     **\rw  5     *****\rx  2     **"
    print(hist("uuaaaxbbbbyyhwawiwjjjwwxym"))


if __name__ == "__main__":
    test()
