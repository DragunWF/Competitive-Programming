# https://www.codewars.com/kata/529fdef7488f509b81000061

def solve(input_string: str) -> str:
    output = []
    values = input_string.split("\n")
    for value in values:
        output.append(count_carries(value))
    return "\n".join(output)


def count_carries(input_string: str) -> str:
    operations = 0

    values = input_string.split(" ")
    first_num = reverse_num(values[0])
    second_num = reverse_num(values[1])
    digit_count = len(first_num)

    carry_num = 0
    for i in range(digit_count):
        first_digit = int(first_num[i])
        second_digit = int(second_num[i])
        result = first_digit + second_digit + carry_num
        if result >= 10:
            operations += 1
            carry_num = result // 10
        else:
            carry_num = 0

    if not operations:
        return "No carry operation"
    return f"{operations} carry operations"


def reverse_num(str_num: str) -> str:
    digits = [*str_num]
    digits.reverse()
    return "".join(digits)


def test() -> None:
    test_cases = [
        "123 456",  # No carry operations
        "555 555",  # 3 carry operations
        "123 594"  # 1 carry operations
    ]
    for test_case in test_cases:
        print(count_carries(test_case))


if __name__ == "__main__":
    test()
