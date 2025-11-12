# https://www.codewars.com/kata/5b043e3886d0752685000009/train/python

def michael_pays(cost: float):
    if cost < 5:
        return float(f"{cost:.2f}")
    kate_contribution = cost / 3
    if kate_contribution > 10:
        kate_contribution = 10
    return float(f"{cost - kate_contribution:.2f}")


def test() -> None:
    print(michael_pays(15))


if __name__ == "__main__":
    test()
