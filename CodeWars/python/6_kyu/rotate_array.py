# https://www.codewars.com/kata/5469e0798a3502f4a90005c9/train/python

def rotate(data: list, n: int) -> list:
    if n == 0:
        return data

    output = [None for item in data]
    for i in range(len(data)):
        output[(i + n) % len(data)] = data[i]
    return output


def test() -> None:
    print(rotate([1, 2, 3, 4, 5], 1))  # [5, 1, 2, 3, 4]
    print(rotate([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]
    print(rotate([1, 2, 3, 4, 5], -1))  # [2, 3, 4, 5, 1]


if __name__ == "__main__":
    test()
