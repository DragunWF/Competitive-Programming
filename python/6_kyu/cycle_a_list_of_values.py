# https://www.codewars.com/kata/5456812629ccbf311b000078/train/python

def cycle(d: int, v: list, c: int) -> list:
    i = -1
    for j in range(len(v)):
        if v[j] == c:
            i = j
            break
    if i == -1:
        return None
    result = i + d
    if result < -len(v) or result >= len(v):
        return v[result % len(v)]
    return v[result]


# Not part of the solution
def test():
    results = (
        cycle(1, [1, 2, 3], 1), cycle(-1, [1, 2, 3], 1),
        cycle(1, [1, 2, 3], 0), cycle(1, [1, 2, 2, 3], 2),
        cycle(1, [*range(0, 70, 3)], 69)
    )
    for result in results:
        print(result)


if __name__ == '__main__':
    test()
