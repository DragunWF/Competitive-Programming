# https://www.codewars.com/kata/68c31c23f0aee823d84cdd42/train/python

def set_the_alarms_up(time: str, n: int) -> str:
    values = time.split(":")
    intervals = [time]
    minutes = int(values[1])
    hour = int(values[0])
    for i in range(n - 1):
        minutes += 5
        intervals.append(
            f"{pad_time((hour + minutes // 60) % 24)}:{pad_time(minutes % 60)}"
        )
    return intervals


def pad_time(value: int) -> str:
    if value <= 9:
        return f"0{value}"
    return str(value)


def test() -> None:
    # Should return ["08:00", "08:05", "08:10", "08:15", "08:20"]
    print(set_the_alarms_up("08:00", 5))
    # Should return ["07:45", "07:50", "07:55", "08:00", "08:05", "08:10", "08:15", "08:20"]
    print(set_the_alarms_up("07:45", 8))
    # Should return ["23:55", "00:00"]
    print(set_the_alarms_up("23:55", 2))


if __name__ == "__main__":
    test()
