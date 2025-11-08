# https://www.codewars.com/kata/5af15a37de4c7f223e00012d/train/python

def men_from_boys(arr: list[int]) -> list[int]:
    even = []
    odd = []
    for num in arr:
        if num % 2 == 0 and not num in even:
            even.append(num)
        elif num % 2 != 0 and not num in odd:
            odd.append(num)
    even.sort()
    odd.sort(reverse=True)
    return [*even, *odd]


def test() -> None:
    print(men_from_boys([7, 3, 14, 17]))  # return (14, 17, 7, 3)


if __name__ == "__main__":
    test()
