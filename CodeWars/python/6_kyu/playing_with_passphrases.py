# https://www.codewars.com/kata/559536379512a64472000053/python

from string import ascii_uppercase


def play_pass(s: str, n: int) -> str:
    words = s.upper().split(" ")
    output = []
    for word in words:
        new_word = ""
        for i, char in enumerate(word):
            if char.isalpha():
                new_letter = ascii_uppercase[(
                    ascii_uppercase.index(char) + n) % 26
                ]
                new_word += new_letter
            elif char.isdigit():
                new_word += str(nines_complement(char))
            else:
                new_word += char
        output.append(new_word)
    return position_case(" ".join(output))[::-1]


def nines_complement(n: str) -> int:
    complement = ""
    for digit in n:
        if digit.isdigit():
            complement += str(9 - int(digit))
    return int(complement)


def position_case(s: str) -> str:
    output = ""
    for i, char in enumerate(s):
        output += char.lower() if i % 2 != 0 else char
    return output


def test() -> None:
    # Expected: "!4897 Oj oSpC"
    print(play_pass("BORN IN 2015!", 1))

    # Expected: "!!!vPz fWpM J"
    print(play_pass("I LOVE YOU!!!", 1))


if __name__ == "__main__":
    test()
