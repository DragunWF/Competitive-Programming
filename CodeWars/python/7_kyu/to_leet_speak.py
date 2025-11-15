# https://www.codewars.com/kata/57c1ab3949324c321600013f/train/python

def to_leet_speak(s: str) -> str:
    letter_map = {
        "A": '@',
        "B": '8',
        "C": '(',
        "D": 'D',
        "E": '3',
        "F": 'F',
        "G": '6',
        "H": '#',
        "I": '!',
        "J": 'J',
        "K": 'K',
        "L": '1',
        "M": 'M',
        "N": 'N',
        "O": '0',
        "P": 'P',
        "Q": 'Q',
        "R": 'R',
        "S": '$',
        "T": '7',
        "U": 'U',
        "V": 'V',
        "W": 'W',
        "X": 'X',
        "Y": 'Y',
        "Z": '2'
    }
    output = ""
    for char in s:
        if not char in letter_map:
            output += char
            continue
        output += letter_map[char]
    return output


def test() -> None:
    print(to_leet_speak("LEET"))  # 1337
    print(to_leet_speak("CODEWARS"))  # (0D3W@R$


if __name__ == "__main__":
    test()
