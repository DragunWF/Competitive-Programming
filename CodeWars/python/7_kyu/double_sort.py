# https://www.codewars.com/kata/57cc79ec484cf991c900018d/train/python

def db_sort(arr: list) -> str:
    num_list = []
    str_list = []
    for item in arr:
        if type(item) is str:
            str_list.append(item)
        elif type(item) is int:
            num_list.append(item)
    num_list.sort()
    str_list.sort()
    return [*num_list, *str_list]


def test() -> None:
    # Expected: [2, 3, 4, 5, 6]
    print(db_sort([6, 2, 3, 4, 5]))


if __name__ == "__main__":
    test()
