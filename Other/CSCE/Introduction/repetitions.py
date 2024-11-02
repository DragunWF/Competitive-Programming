# https://cses.fi/problemset/task/1069

if __name__ == "__main__":
    s = input()
    longest, current = 1, 1
    prev = None
    for i, char in enumerate(s):
        if char == prev:
            current += 1
        else:
            current = 1
            prev = char
        if current > longest:
            longest = current
    print(longest)
