# https://www.codewars.com/kata/57470efebf81fea166001627/train/python

def letter_check(arr: str) -> str:
    first_str, second_str = arr[0].lower(), arr[1].lower()
    for char in second_str:
        if not char in first_str:
            return False
    return True


def test() -> None:
    print(letter_check(["trances", "nectar"]))  # True


if __name__ == "__main__":
    test()
