# https://www.codewars.com/kata/5a34f087c5e28462d9000082

def swap_head_tail(arr: list) -> list:
    N = len(arr)
    half = N // 2
    if N % 2 == 0:
        return [*arr[half:N], *arr[0:half]]
    return [*arr[half + 1:N], arr[half], *arr[0:half]]


def test() -> None:
    print(swap_head_tail([1, 2, 3, 4, 5]))


if __name__ == "__main__":
    test()
