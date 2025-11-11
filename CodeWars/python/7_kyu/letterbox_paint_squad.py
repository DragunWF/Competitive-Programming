# https://www.codewars.com/kata/597d75744f4190857a00008d

def paint_letterboxes(start: int, finish: int) -> list[int]:
    output = [0 for i in range(10)]
    for num in range(start, finish + 1):
        str_num = str(num)
        for digit in str_num:
            output[int(digit)] += 1
    return output


def test() -> None:
    print(paint_letterboxes(125, 132))  # [1,9,6,3,0,1,1,1,1,1]


if __name__ == "__main__":
    test()
