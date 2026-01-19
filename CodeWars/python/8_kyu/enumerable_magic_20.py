# https://www.codewars.com/kata/545af3d185166a3dec001190

def each_cons(lst: list, n: int) -> list:
    output = []
    for i in range(len(lst)):
        end = i + n
        if end > len(lst):
            break
        cascade_item = []
        for j in range(i, end):
            cascade_item.append(lst[j])
        output.append(cascade_item)
    return output


def test() -> None:
    # => [[1,2], [2,3], [3,4]]
    print(each_cons([1, 2, 3, 4], 2))

    # => [[1,2,3],[2,3,4]]
    print(each_cons([1, 2, 3, 4], 3))


if __name__ == "__main__":
    test()
