# https://www.codewars.com/kata/5862f663b4e9d6f12b00003b


def guess_blue(blue_start: int, red_start: int, blue_pulled: int, red_pulled: int) -> int:
    remaining_blue_marbles = blue_start - blue_pulled
    remaining_red_marbles = red_start - red_pulled
    total_marbles = remaining_red_marbles + remaining_blue_marbles
    return remaining_blue_marbles / total_marbles


def test() -> None:
    print(guess_blue(5, 5, 2, 3))  # 0.6


if __name__ == "__main__":
    test()
