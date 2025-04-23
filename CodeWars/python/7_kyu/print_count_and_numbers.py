# https://www.codewars.com/kata/559af787b4b8eac78b000022/train/python

def count_me(data: str) -> str:
    if not data or not data.isdigit():
        return ""
    output = ""
    current_count = 0
    for i, char in enumerate(data):
        if i == 0:
            current_count += 1
            continue
        if char == data[i - 1]:
            current_count += 1
        else:
            output += f"{current_count}{data[i - 1]}"
            current_count = 1
    output += f"{current_count}{data[-1]}"
    return output


def test() -> None:
    print(count_me("21"))  # 1211
    print(count_me("1211"))  # 111221
    print(count_me("123a"))  # ""


if __name__ == "__main__":
    test()
