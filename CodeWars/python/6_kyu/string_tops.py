# https://www.codewars.com/kata/59b7571bbf10a48c75000070/train/python

def tops(msg: str) -> str:
    if len(msg) < 2:
        return ""
    output = msg[1]
    target_gap = 4
    current_gap = 0
    for i in range(2, len(msg) + 1):
        current_gap += 1
        if current_gap == target_gap + 1:
            output += msg[i]
            target_gap += 4
            current_gap = 0
    return output[::-1]


def test() -> None:
    # Expected: 3pgb
    print(tops("abcdefghijklmnopqrstuvwxyz1234"))


if __name__ == "__main__":
    test()
