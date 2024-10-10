# https://www.codewars.com/kata/5297bf69649be865e6000922/train/python

def make_sentences(parts: list[str]) -> str:
    parts = trim_periods(parts)
    for i in range(1, len(parts)):
        if parts[i] == ",":
            parts[i] = ""
            parts[i - 1] = f"{parts[i - 1]},"
    while "" in parts:
        parts.remove("")
    return f"{' '.join(parts)}."


def trim_periods(parts: list[str]) -> list[str]:
    start_of_no_period = None
    for i in range(len(parts) - 1, -1, -1):
        if parts[i] != ".":
            start_of_no_period = i
            break
    return parts[0:start_of_no_period + 1]


def test():
    # Not part of the solution
    print(make_sentences(['hello', ',', 'my', 'dear']))  # 'hello, my dear.'


if __name__ == "__main__":
    test()
