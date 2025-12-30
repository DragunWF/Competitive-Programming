# https://www.codewars.com/kata/559f860f8c0d6c7784000119/train/python

def any_arrows(arrows: list[dict]) -> bool:
    if not arrows:
        return False
    return not all("damaged" in arrow and arrow["damaged"] for arrow in arrows)


def test() -> None:
    # Expected: False
    print(any_arrows(
        [{'range': 5}, {'range': 10, 'damaged': True},
         {'damaged': True}]
    ))

    # Expected: True
    print(any_arrows(
        [{'range': 5}, {'range': 10, }]
    ))


if __name__ == "__main__":
    test()
