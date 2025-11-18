# https://www.codewars.com/kata/56e56756404bb1c950000992

from math import lcm


def sum_differences_between_products_and_LCMs(pairs: list[list[int, int]]) -> int:
    products = []
    lcms = []
    for pair in pairs:
        lcms.append(lcm(pair[0], pair[1]))
        products.append(pair[0] * pair[1])
    total = 0
    for i in range(len(pairs)):
        total += products[i] - lcms[i]
    return total


def test() -> None:
    # Expected: 840
    print(sum_differences_between_products_and_LCMs(
        [[15, 18], [4, 5], [12, 60]]))


if __name__ == "__main__":
    test()
