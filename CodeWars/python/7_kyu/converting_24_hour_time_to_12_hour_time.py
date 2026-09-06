# https://www.codewars.com/kata/59b0ab12cf3395ef68000081/train/python

def to_12_hour_time(time_string: str) -> str:
    hours = int(time_string[0] + time_string[1])
    minutes = str(int(time_string[2] + time_string[3]))
    meridiem = 'pm' if hours >= 12 else 'am'
    hours %= 12
    if hours == 0:
        hours = 12
    return f"{hours}:{minutes.rjust(2, '0')} {meridiem}"


def test() -> None:
    # 1:00 pm
    print(to_12_hour_time("1300"))


if __name__ == "__main__":
    test()
