def solve(s: str):
    uppercase, lowercase = 0, 0
    for character in s:
        if character == character.lower():
            lowercase += 1
        else:
            uppercase += 1
    return s.lower() if lowercase >= uppercase else s.upper()


def main():
    s = input()
    print(solve(s))


main()
