# https://www.codewars.com/kata/5865cff66b5699883f0001aa/train/python

def to_time(seconds: int) -> str:
    minutes = seconds // 60
    hours = minutes // 60
    return f"{hours} hour(s) and {minutes % 60} minute(s)"


def test() -> None:
    print(to_time(3600))  # --> "1 hour(s) and 0 minute(s)"
    print(to_time(3601))  # --> "1 hour(s) and 0 minute(s)"
    print(to_time(3500))  # --> "0 hour(s) and 58 minute(s)"
    print(to_time(323500))  # --> "89 hour(s) and 51 minute(s)"


if __name__ == "__main__":
    test()
