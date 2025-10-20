# https://www.codewars.com/kata/572ab0cfa3af384df7000ff8/train/python

def shuffle_it(arr: list[int], *swaps: list[list[int]]) -> list[int]:
    for swap in swaps:
        temp = arr[swap[0]]
        arr[swap[0]] = arr[swap[1]]
        arr[swap[1]] = temp
    return arr


def test() -> None:
    print(shuffle_it([1, 2, 3, 4, 5], [1, 2]))


if __name__ == "__main__":
    test()
