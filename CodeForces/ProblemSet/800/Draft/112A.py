from string import ascii_lowercase as letters


def solve(a, b):
    alphabets = tuple([*letters])
    strings = (a, b)
    val_a, val_b = 0, 0

    for i in range(2):
        for character in strings[i]:
            if i == 0:
                val_a += alphabets.index(character)
            else:
                val_b += alphabets.index(character)

    if val_a == val_b:
        return 0
    return -1 if val_a < val_b else 1


def main():
    a, b = input().lower(), input().lower()
    print(solve(a, b))


main()
