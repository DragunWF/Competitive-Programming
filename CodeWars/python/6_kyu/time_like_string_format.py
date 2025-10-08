# https://www.codewars.com/kata/51e000d070fe4414000003f0/train/python

def solution(hour: int) -> str:
    if hour < 100 or hour > 9999:
        raise Exception("Invalid time format!")

    str_hour = str(hour)
    digit_count = len(str_hour)
    if digit_count == 3:
        return f"{str_hour[0]}:{str_hour[1]}{str_hour[2]}"
    return f"{str_hour[0]}{str_hour[1]}:{str_hour[2]}{str_hour[3]}"


def test() -> None:
    print(solution(800))  # 8:00
    print(solution(1000))  # 10:00


if __name__ == "__main__":
    test()
