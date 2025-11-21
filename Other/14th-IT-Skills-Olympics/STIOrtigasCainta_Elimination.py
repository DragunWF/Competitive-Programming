def solve() -> None:
    print("=== ARMSTRONG NUMBER TOOL ===")
    number = int(input("Enter a non-negative integer to check: "))
    if number < 0:
        print("Integer must not be negative!")
        return
    if minimum_is_armstrong(number):
        print(f"{number} is an Armstrong number")
    else:
        print(f"{number} is not an Armstrong number")
    str_num = str(number)
    print(f"Digits: {', '.join([*str_num])}")
    print(f"Number of digits: {len(str_num)}")
    display_computed_sum(number)

    print("Thank you for using the Armstrong Number Tool.")


def minimum_is_armstrong(n: int) -> bool:
    return digit_power_sum(n) == n


def digit_power_sum(n: int) -> int:
    str_num = str(n)
    digit_count = len(str_num)
    result = 0
    for i in range(digit_count):
        result += int(str_num[i]) ** digit_count
    return result


def display_computed_sum(n: int) -> None:
    str_num = str(n)
    digit_count = len(str_num)
    output = []
    for digit in str_num:
        output.append(f"{digit}^{digit_count}")
    print("Computed Sum:", " + ".join(output) + " = " + str(digit_power_sum(n)))


if __name__ == "__main__":
    solve()