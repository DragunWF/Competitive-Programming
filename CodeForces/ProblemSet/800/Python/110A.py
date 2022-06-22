def solve(n):
    lucky_digits = 0
    for digit in n:
        if digit == "4" or digit == "7":
            lucky_digits += 1
    if lucky_digits == 4 or lucky_digits == 7:
        return "YES"
    return "NO"


def main():
    n = input()
    print(solve(n))


main()
