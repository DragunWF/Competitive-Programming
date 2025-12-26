# https://www.codewars.com/kata/80-s-kids-number-1-how-many-licks-does-it-take

def total_licks(env: dict):
    licks = 252
    toughest_challenge = None
    max_challenge = 0
    for condition, value in env.items():
        licks += value
        if value > max_challenge:
            toughest_challenge = condition
            max_challenge = value
    output = f"It took {licks} licks to get to the tootsie roll center of a tootsie pop."
    if not toughest_challenge is None:
        output += f" The toughest challenge was {toughest_challenge}."
    return output


def test() -> None:
    # Expected: 260
    print(total_licks({"freezing temps": 10, "clear skies": -2}))


if __name__ == "__main__":
    test()
