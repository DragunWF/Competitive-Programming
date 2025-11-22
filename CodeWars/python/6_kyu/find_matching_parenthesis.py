# https://www.codewars.com/kata/59293c2cfafd38975600002d/train/python

def find_paren_match(s: str, pos: int) -> str:
    if s[pos] != "(" and s[pos] != ")":
        return -1

    if s[pos] == "(":
        opened = 0
        for i in range(pos, len(s)):
            char = s[i]
            if char == "(":
                opened += 1
            elif char == ")":
                opened -= 1
                if opened == 0:
                    return i
    else:
        closed = 0
        for i in range(pos, -1, -1):
            char = s[i]
            if char == ")":
                closed += 1
            elif char == "(":
                closed -= 1
                if closed == 0:
                    return i


def test() -> None:
    print(find_paren_match('(som(th)ng)', 0))  # 10
    print(find_paren_match('(som(th)ng)', 4))  # 7
    print(find_paren_match('(som(th)ng)', 2))  # -1
    print(find_paren_match('(som(th)ng)', 10))  # 0


if __name__ == "__main__":
    test()
