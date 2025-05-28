# https://www.codewars.com/kata/56459c0df289d97bd7000083/train/python

def generator(_from, _to, _step):
    if _step <= 0:
        return []

    output = []
    if _from < _to:
        for i in range(_from, _to + 1, _step):
            output.append(i)
    else:
        for i in range(_from, _to - 1, -_step):
            output.append(i)
    return output


def test() -> None:
    print(generator(20, 10, 1))


if __name__ == "__main__":
    test()
