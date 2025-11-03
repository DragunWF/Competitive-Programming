# https://www.codewars.com/kata/57873ab5e55533a2890000c7

def time_correct(t: str) -> str:
    if not t:
        return t
    if not is_valid_time_format(t):
        return None

    values = list(map(int, t.split(":")))
    seconds = values[2]
    additional_minutes = 0
    if seconds >= 60:
        additional_minutes = seconds // 60
        seconds %= 60
    minutes = values[1] + additional_minutes
    additional_hours = 0
    if minutes >= 60:
        additional_hours = minutes // 60
        minutes %= 60

    hours = pad_time_element((values[0] + additional_hours) % 24)
    minutes = pad_time_element(minutes)
    seconds = pad_time_element(seconds)
    return f"{hours}:{minutes}:{seconds}"


def is_valid_time_format(t: str) -> bool:
    values = t.split(":")
    if len(values) != 3:
        return False
    for element in values:
        if len(element) != 2 or not element.isdigit():
            return False
    return True


def pad_time_element(element: int) -> str:
    if element == 0:
        return "00"
    if element < 10:
        return f"0{element}"
    return str(element)


def test() -> None:
    test_cases = [
        "09:10:01",
        "11:70:10",
        "19:99:99",
        "24:01:01",
        "4:32:09"
    ]
    expected = [
        "09:10:01",
        "12:10:10",
        "20:40:39",
        "00:01:01",
        None
    ]
    print("+--- Test Cases ---+\n")
    for i in range(len(test_cases)):
        item = test_cases[i]
        result = time_correct(item)
        print("Test Case:", item)
        print("Result:", time_correct(item))
        print("Pass:", result == expected[i])
        print()
    print("+------------------+")


if __name__ == "__main__":
    test()
