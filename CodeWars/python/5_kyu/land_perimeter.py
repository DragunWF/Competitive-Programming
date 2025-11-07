# https://www.codewars.com/kata/5839c48f0cf94640a20001d3/train/python

def land_perimeter(arr: list[str]) -> str:
    total_perimeter = 0
    for i in range(len(arr)):
        row = arr[i]
        top_row = None
        bottom_row = None

        if i != 0:
            top_row = arr[i - 1]
        if i != len(arr) - 1:
            bottom_row = arr[i + 1]

        for j in range(len(row)):
            if row[j] == "O":
                continue

            if j == 0 or (j != 0 and row[j - 1] == "O"):
                total_perimeter += 1
            if j == len(row) - 1 or (j != len(row) - 1 and row[j + 1] == "O"):
                total_perimeter += 1
            if not top_row or (top_row and top_row[j] == "O"):
                total_perimeter += 1
            if not bottom_row or (bottom_row and bottom_row[j] == "O"):
                total_perimeter += 1
    return f"Total land perimeter: {total_perimeter}"


def test() -> None:
    print(land_perimeter(['XOOXO',
                          'XOOXO',
                          'OOOXO',
                          'XXOXO',
                          'OXOOO']))  # 24


if __name__ == "__main__":
    test()
