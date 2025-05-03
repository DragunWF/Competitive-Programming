# https://www.codewars.com/kata/58311faba317216aad000168/train/python

def print_nums(*args: list) -> str:
    if not args:
        return ""
    
    output = []
    max_digit_count = max(len(str(num)) for num in args)
    for num in args:
        digit_count = len(str(num))
        output.append(("0" * (max_digit_count - digit_count)) + str(num))
    return "\n".join(output)
