def solve() -> None:
    year = int(input("Enter a year: "))
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")


def is_leap_year(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False

if __name__ == "__main__":
    solve()