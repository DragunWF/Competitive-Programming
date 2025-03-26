# https://www.codewars.com/kata/5ac54bcbb925d9b437000001/train/python

def find_middle(s: str) -> int:
    if not s or type(s) != str:
        return - 1

    number_str = get_number(s)
    if not number_str:
        return -1

    product_str = get_product(number_str)
    middle = len(product_str) // 2
    if len(product_str) % 2 == 0:
        return int(f"{product_str[middle - 1]}{product_str[middle]}")
    return int(product_str[middle])


def get_number(s: str) -> str:
    output = ""
    for char in s:
        if char.isdigit():
            output += char
    return output


def get_product(num_str: str) -> str:
    output = int(num_str[0])
    for i in range(1, len(num_str)):
        output *= int(num_str[i])
    return str(output)
