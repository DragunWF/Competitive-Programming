# https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5/train/python
from rich import print


def parse_int(string: str) -> int:
    if string == "one million":
        return 1000000

    words = [x for x in string.split(" ") if x != "and"]
    length = len(words)
    if length == 1:
        if "-" in words[0]:
            return parse_tenths(words[0])
        return parse_word(words[0])

    output = 0
    if "thousand" in words:
        words = " ".join(words).split("thousand")
        output += parse_thousands(words[0])
        if length > 1:
            output += parse_hundreds(words[1])
    else:
        output += parse_hundreds(" ".join(words))

    return output


def parse_tenths(string: str) -> int:
    nums = string.split("-")
    return parse_word(nums[0]) + parse_word(nums[1])


def parse_hundreds(string: str) -> int:
    nums = [x for x in string.split(" ") if x]
    output, length = 0, len(nums)
    for i in range(length):
        if nums[i] == "hundred" or nums[i] == "thousand":
            continue
        elif i + 1 != length and nums[i + 1] == "hundred":
            output += parse_word(nums[i]) * 100
        elif "-" in nums[i]:
            output += parse_tenths(nums[i])
        else:
            output += parse_word(nums[i])
    return output


def parse_thousands(string: str) -> int:
    return parse_hundreds(string) * 1000


def parse_word(word: str) -> int:
    # forgive me father for I have sinned
    unique_num = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
    }
    return unique_num[word]


test_cases = (
    "one million",
    "forty-five",
    "two hundred forty-six",
    "one hundred thousand",
    "three hundred thousand forty-three",
    "eighty-three thousand",
    "five hundred twenty-one thousand one hundred forty-three",
    "one hundred one"
)
for case in test_cases:
    print(parse_int(case))
