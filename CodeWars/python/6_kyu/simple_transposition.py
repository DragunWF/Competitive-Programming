# https://www.codewars.com/kata/57a153e872292d7c030009d4/train/python

def simple_transposition(text: str) -> str:
    encrypted = ["", ""]
    for i, char in enumerate(text):
        encrypted[i % 2] += char
    return "".join(encrypted)


def test():
    output = simple_transposition("MEETMEAFTERTHETOGAPARTY")
    expected_output = "MEMATRHTGPRYETEFETEOAAT"
    print(output, output == expected_output)


if __name__ == "__main__":
    test()
