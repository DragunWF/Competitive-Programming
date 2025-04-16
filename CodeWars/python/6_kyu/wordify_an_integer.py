# https://www.codewars.com/kata/553a2461098c64ae53000041/train/python

def wordify(n: int) -> str:
    special_cases = {10: "ten", 11: "eleven", 12: "twelve",
                     13: "thirteen", 14: "fourteen", 15: "fifteen",
                     16: "sixteen", 17: "seventeen", 18: "eighteen",
                     19: "nineteen"}
    if n in special_cases:
        return special_cases[n]

    num_words = []
    str_num = str(n)

    ones_words = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
                  6: "six", 7: "seven", 8: "eight", 9: "nine"}
    tenths_words = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty",
                    6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}

    if n <= 9:
        return ones_words[n]
    if n >= 10:
        ones_digit = int(str_num[-1])
        tenths_digit = int(str_num[-2])

        if tenths_digit == 1:
            tenths_key = int(f"{tenths_digit}{ones_digit}")
            num_words.append(special_cases[tenths_key])
        else:
            if tenths_digit != 0:
                num_words.append(tenths_words[tenths_digit])
            if ones_digit != 0:
                num_words.append(ones_words[ones_digit])
    if n >= 100:
        hundreds_digit = int(str_num[-3])
        num_words.insert(0, f"{ones_words[hundreds_digit]} hundred")

    return " ".join(num_words)


def test() -> None:
    print(wordify(326))
    print(wordify(56))


if __name__ == "__main__":
    test()
