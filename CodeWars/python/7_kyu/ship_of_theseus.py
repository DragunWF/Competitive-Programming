# https://www.codewars.com/kata/69b83710b26939b35fd10429/train/python

def ship_of_theseus(ship: list) -> bool:
    if len(ship) <= 1:
        return True
    if len(set([len(state) for state in ship])) != 1:
        return False

    prev_state = None
    for i, state in enumerate(ship):
        if i == 0:
            prev_state = state
            continue
        changes = 0
        for j in range(len(state)):
            if state[j] != prev_state[j]:
                changes += 1
            if changes >= 2:
                return False
        if changes != 1:
            return False
        prev_state = state
    return True


def test() -> None:
    # Expected: true
    print(ship_of_theseus([
        ["a", "b", "c"],
        ["x", "b", "c"],
        ["x", "y", "c"],
        ["x", "y", "z"]
    ]))

    # Expected: false
    print(ship_of_theseus([
        ["a", "b", "c"],
        ["x", "y", "c"]
    ]))


if __name__ == "__main__":
    test()
