# https://www.codewars.com/kata/606b43f4adea6e00425dff42/train/python

def grid_map(inp: list[list], op) -> list:
    output = []
    for arr in inp:
        row = []
        for item in arr:
            row.append(op(item))
        output.append(row)
    return output


def test() -> None:
    print(grid_map([[1, 2, 3],
                    [4, 5, 6]], lambda x: x ** 2))


if __name__ == "__main__":
    test()
