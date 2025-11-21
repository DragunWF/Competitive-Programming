def solve() -> None:
    odd_number = int(input("Enter an odd number for the diamond suze (1-19): "))
    if odd_number % 2 == 0:
        print("input ODD number only")
        return
    if not (1 <= odd_number <= 19):
        print("Number must be within the range of 1 and 19")
        return
    print_diamond(odd_number)


def print_diamond(size: int) -> None:
    mid = size // 2
    whitespace_count = size - 1
    asterisk_count = 1
    for i in range(size):
        line = ""

        if whitespace_count > 0:
            line += whitespace_count * " "
        asterisks = []
        for j in range(asterisk_count):
            asterisks.append("*")
        line += " ".join(asterisks)
        if whitespace_count > 0:
            line += whitespace_count * " "
        print(line)

        if i < mid:
            asterisk_count += 2
            whitespace_count -= 2
        else:
            asterisk_count -= 2
            whitespace_count += 2


if __name__ == "__main__":
    solve()
