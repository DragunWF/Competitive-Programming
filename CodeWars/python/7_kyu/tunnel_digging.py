# https://www.codewars.com/kata/626466bdd13ea6923d0663ea/train/python

def tunnel_digging(r: list[str]) -> int:
    total_minutes = 0
    for i, section in enumerate(r):
        for rock in section:
            total_minutes += get_time(rock)
        if (i + 1) % 3 == 0:
            total_minutes += 30
    return total_minutes


def get_time(rock: str) -> int:
    time = {"[]": 30, "{}": 25, "()": 20, "||": 15, "::": 10}
    for key, value in time.items():
        if rock in key:
            return value
    return 0


def test():
    # Just testing, not part of the solution
    print(tunnel_digging([': ', '  ', ': ']))  # 50


if __name__ == "__main__":
    test()
