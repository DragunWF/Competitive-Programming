# https://www.codewars.com/kata/5aee86c5783bb432cd000018

def hydrate(drink_string: str) -> str:
    glasses_count = 0
    tokens = drink_string.split(" ")
    for token in tokens:
        if token.isdigit():
            glasses_count += int(token)
    return f"{glasses_count} {'glasses' if glasses_count != 1 else 'glass'} of water"


def test() -> None:
    # Expected: 10 glasses of water
    print(hydrate("1 shot, 5 beers, 2 shots, 1 glass of wine, 1 beer"))


if __name__ == "__main__":
    test()
