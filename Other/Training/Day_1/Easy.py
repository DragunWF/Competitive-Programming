import sys
from collections import Counter

def solve() -> None:
    sys.stdout.write("String: ")
    user_input = sys.stdin.readline()
    counter = Counter(char for char in user_input if char.isalpha())
    for key in counter:
        sys.stdout.write(f"{key}: {counter[key]}\n")


if __name__ == "__main__":
    solve()