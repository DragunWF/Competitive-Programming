# https://www.codewars.com/kata/599febdc3f64cd21d8000117/train/python

def numbers_of_letters(n: int) -> list[str]:
    if n == 4:
        return ["four"]
    output = [get_num_word(n)]
    output.append(get_num_word(len(output[-1])))
    while len(output[-2]) != len(output[-1]):
        output.append(get_num_word(len(output[-1])))
    return output


def get_num_word(n: int) -> str:
    numbers = ("zero", "one", "two", "three", "four",
               "five", "six", "seven", "eight", "nine")
    str_n = str(n)
    return "".join(numbers[int(str_n[i])] for i in range(len(str_n)))


def test():
    print(get_num_word(12))  # "onetwo"
    print(numbers_of_letters(12))  # ["onetwo", "six", "three", "five", "four"]


if __name__ == "__main__":
    test()
