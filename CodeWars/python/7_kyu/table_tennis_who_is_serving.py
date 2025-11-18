# https://www.codewars.com/kata/679e3754cb041c0685865dde/python

def who_is_serving(current_round: int) -> int:
    current_player = 1
    rounds_left_for_player = 2
    round = 1
    while round < current_round:
        round += 1
        rounds_left_for_player -= 1
        if rounds_left_for_player == 0:
            current_player = 2 if current_player == 1 else 1
            rounds_left_for_player = 2
    return current_player


def test() -> None:
    print(who_is_serving(8))


if __name__ == "__main__":
    test()
