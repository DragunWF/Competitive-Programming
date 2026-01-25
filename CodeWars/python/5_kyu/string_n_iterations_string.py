# https://www.codewars.com/kata/5ae43ed6252e666a6b0000a4/train/python

def jumbled_string(s: str, n: int) -> str:
    if n <= 0 or len(s) < 2:
        return s
    original = s
    for i in range(n):
        s = s[::2] + s[1::2]
        if s == original:
            cycle_len = i + 1
            remaining_steps = (n - (i + 1)) % cycle_len
            for j in range(remaining_steps):
                s = s[::2] + s[1::2]
            return s
    return s


def jumbled_string_recursion(s: str, n: int) -> str:
    if n <= 0:
        return s
    front, back = [], []
    for i, char in enumerate(s):
        if i % 2 == 0:
            front.append(char)
        else:
            back.append(char)
    return jumbled_string_recursion("".join(front) + "".join(back), n - 1)


def test() -> None:
    # Expected: "WwEapeo xml!"
    print(jumbled_string("Wow Example!", 1))

    # Expected: "qtorieuwy"
    print(jumbled_string("qwertyuio", 2))


if __name__ == "__main__":
    test()
