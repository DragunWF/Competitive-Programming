# https://www.codewars.com/kata/5a941f4e1a60f6e8a70025fe

def odd_ball(arr: list) -> bool:
    for num in arr:
        if type(num) is int and num < len(arr) and arr[num] == "odd":
            return True
    return False


def test() -> None:
    # Expected: True
    print(odd_ball(["even", 4, "even", 7, "even", 55,
          "even", 6, "even", 10, "odd", 3, "even"]))


if __name__ == "__main__":
    test()
