# https://www.codewars.com/kata/597bb84522bc93b71e00007e/train/python

def string_merge(string1: str, string2: str, letter: str) -> str:
    output = ""
    for char in string1:
        output += char
        if char == letter:
            break
    letter_found = False
    for char in string2:
        if letter_found:
            output += char
        if char == letter:
            letter_found = True
    return output


def test() -> None:
    print(string_merge("hello", "world", "l"))       # ==>  "held"
    print(string_merge("coding", "anywhere", "n"))   # ==>  "codinywhere"
    print(string_merge("jason", "samson", "s"))      # ==>  "jasamson"
    print(string_merge("wonderful", "people", "e"))  # ==>  "wondeople"


if __name__ == "__main__":
    test()
