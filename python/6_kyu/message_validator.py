# https://www.codewars.com/kata/5fc7d2d2682ff3000e1a3fbc/train/python

from string import digits


def is_a_valid_message(message: str) -> bool:
    if not message:
        return True
    if message[-1] in digits:
        return False
    message = split_message(message)
    try:
        for i in range(0, len(message), 2):
            if int(message[i]) != len(message[i + 1]):
                return False
    except:
        return False
    return True


def split_message(message: str) -> list[str]:
    output = []
    current_item = ""
    is_digit_item = False
    for i, char in enumerate(message):
        is_digit_item = char in digits
        if is_digit_item and not message[i - 1] in digits or not is_digit_item and message[i - 1] in digits:
            if current_item:
                output.append(current_item)
            current_item = ""
        current_item += char
    output.append(current_item)
    return output


def test():
    print(split_message("3hey5hello2hi"))
    print(split_message("4code13hellocodewars"))
    print(is_a_valid_message("3hey5hello2hi"))


if __name__ == '__main__':
    test()
