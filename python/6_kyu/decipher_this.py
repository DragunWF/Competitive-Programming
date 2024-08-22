# https://www.codewars.com/kata/581e014b55f2c52bb00000f8/train/python

from string import digits


def decipher_this(s: str) -> str:
    words = s.split(" ")
    output = []
    for word in words:
        output.append(decrypt(word))
    return " ".join(output)


def decrypt(word: str) -> str:
    output = []
    char_code = ""
    for char in word:
        if char in digits:
            char_code += char
        else:
            break
    output.append(chr(int(char_code)))
    for i in range(len(char_code), len(word)):
        output.append(word[i])
    if (len(word) - len(char_code) + 1) > 2:
        output[1], output[-1] = output[-1], output[1]
    return "".join(output)


def test():
    # Not part of the solution, just testing
    print(decipher_this("72olle 103doo 100ya"))


if __name__ == "__main__":
    test()
