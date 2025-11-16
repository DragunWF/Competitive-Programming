# https://www.codewars.com/kata/55960bbb182094bc4800007b/train/python

def insert_dash(num: int) -> str:
    str_num = str(num)
    if num <= 9:
        return str_num
    output = str_num[0]
    for i in range(1, len(str_num)):
        if int(str_num[i - 1]) % 2 != 0 and int(str_num[i]) % 2 != 0:
            output += "-"
        output += str_num[i]
    return output


def test() -> None:
    print(insert_dash(454793))  # "4547-9-3"


if __name__ == "__main__":
    test()
