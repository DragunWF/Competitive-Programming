# https://www.codewars.com/kata/671fd30696d3f42285f7d1f1/train/python

def window(lngth, offset, lst):
    if not lngth:
        return [[] for i in range(len(lst))]

    i = 0
    output = []
    while i < len(lst):
        subset = []
        target_reach = i + lngth
        if target_reach > len(lst):
            break
        for j in range(i, i + lngth):
            subset.append(lst[j])
        output.append(subset)
        i += offset
    return output


def test() -> None:
    print(window(2, 1, [0, 1, 2, 3, 4]))
    print(window(2, 2, [0, 1, 2, 3, 4]))
    print(window(0, 2, [0]))


if __name__ == "__main__":
    test()
