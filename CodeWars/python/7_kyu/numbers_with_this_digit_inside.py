# https://www.codewars.com/kata/58880c6e79a0a3e459000004

def numbers_with_digit_inside(x: int, d: int) -> list[int]:
    numbers = []
    d = str(d)
    for num in range(1, x + 1):
        str_num = str(num)
        if d in str_num:
            numbers.append(num)
    sum_of_nums = 0 if not numbers else numbers[0]
    product_of_nums = 0 if not numbers else numbers[0]
    for i in range(1, len(numbers)):
        sum_of_nums += numbers[i]
        product_of_nums *= numbers[i]
    return [len(numbers), sum_of_nums, product_of_nums]


def test() -> None:
    # Expected: [3, 22, 110]
    print(numbers_with_digit_inside(11, 1))


if __name__ == "__main__":
    test()
