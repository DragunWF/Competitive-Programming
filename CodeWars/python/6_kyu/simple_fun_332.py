# https://www.codewars.com/kata/5954584610080b7252000003

def catch_thief(queue: str) -> int:
    caught_thieves = 0
    watched = [False for i in range(len(queue))]
    for i, char in enumerate(queue):
        if char.isdigit():
            watched[i] = True
            watch_range = int(char)
            for j in range(i, max(i - watch_range - 1, -1), -1):
                watched[j] = True
            for j in range(i, min(i + watch_range + 1, len(queue))):
                watched[j] = True
    for i, char in enumerate(queue):
        if char == "X" and watched[i]:
            caught_thieves += 1
    return caught_thieves


def test() -> None:
    print(catch_thief("X5X#3X###XXXX##1#X1X"))  # 5


if __name__ == "__main__":
    test()
