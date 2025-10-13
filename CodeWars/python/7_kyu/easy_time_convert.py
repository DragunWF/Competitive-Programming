# https://www.codewars.com/kata/5a084a098ba9146690000969/train/python

def time_convert(num: int) -> str:
    if num <= 0:
        return "00:00"

    hour = num // 60
    minute = num % 60
    if minute <= 9:
        minute = "0" + str(minute)
    if hour <= 9:
        hour = "0" + str(hour)
    return f"{hour}:{minute}"


def test() -> None:
    print(time_convert(78))  # 01:18


if __name__ == "__main__":
    test()
