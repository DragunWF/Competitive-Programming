# https://www.codewars.com/kata/5506b230a11c0aeab3000c1f/train/python

def evaporator(content: int, evap_per_day: int, threshold: int) -> int:
    days = 0
    initial_content = content
    while content >= (initial_content * (threshold / 100)):
        content -= content * (evap_per_day / 100)
        days += 1
    return days


def test() -> None:
    print(evaporator(10, 10, 5))  # 29


if __name__ == "__main__":
    test()
