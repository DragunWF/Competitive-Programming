# https://www.codewars.com/kata/586d12f0aa042830910001d1

def remove_char(array: list[str]) -> list[str]:
    output = []
    for item in array:
        digits = []
        for char in item:
            if char.isdigit():
                digits.append(char)
        whole_num = "".join(digits[:-2])
        decimal_num = "".join(digits[-2:])
        output.append(f"${whole_num}.{decimal_num}")
    return output


def test() -> None:
    # Expected: ['$56.64', '$33.59', '$29.49', '$94.20', '$44.94']
    print(remove_char(['$5.$6.6x.s4', '{$33ae.5(9', '$29..4e9', '%.$9|4d20', 'A$AA$4r R4.94']))


if __name__ == "__main__":
    test()
