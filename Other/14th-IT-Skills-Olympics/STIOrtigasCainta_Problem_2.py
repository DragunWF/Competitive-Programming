def solve() -> None:
    is_valid = False
    num = None
    int_num = None
    while not is_valid:
        num = input("Enter a number to be reversed: ")
        if not num.isdigit():
            print("Number is not numeric!")
            continue

        int_num = int(num)
        if int_num < 0:
            print("Number must not be negative!")
            continue

        is_valid = True
    print(f"{num} =>", end=" ")
    print_reversed_num(int_num, len(num))


def print_reversed_num(num: int, digit_count: int) -> None:
    reversed_num = 0
    missing_zeros = 0
    for i in range(digit_count):
        last_digit = num % 10
        reversed_num = reversed_num * 10 + last_digit
        num //= 10
    if not missing_zeros:
        print(reversed_num)
    else:
        for i in range(missing_zeros):
            print("0", end="")
            print(reversed_num)


if __name__ == "__main__":
    solve()
