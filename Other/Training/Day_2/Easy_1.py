import sys


def solve() -> None:
    sys.stdout.write("Celsius: ")
    fahrenheit = celsius_to_fahrenheit(float(sys.stdin.readline()))
    print(f"Fahrenheit: {fahrenheit}")


def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32


if __name__ == "__main__":
    solve()