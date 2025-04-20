# https://www.codewars.com/kata/5705c699cb729350870003b7/train/python

def string_color(name: str) -> str:
    if len(name) < 2:
        return None

    first_char_value = ord(name[0])
    ascii_sum, ascii_product = first_char_value, first_char_value
    for i in range(1, len(name)):
        ascii_value = ord(name[i])
        ascii_sum += ascii_value
        ascii_product *= ascii_value

    last_ascii_value = abs(first_char_value - (ascii_sum - first_char_value))
    return f"{trim_hex(ascii_sum)}{trim_hex(ascii_product)}{trim_hex(last_ascii_value)}"


def trim_hex(num: int) -> str:
    trimmed = hex(num % 256)[2:].upper()
    return f"0{trimmed}" if len(trimmed) == 1 else trimmed


def test() -> None:
    print(string_color("Jack"))


if __name__ == "__main__":
    test()
