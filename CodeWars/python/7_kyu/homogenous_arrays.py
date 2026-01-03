# https://www.codewars.com/kata/57ef016a7b45ef647a00002d

def filter_homogenous(arrays: list) -> list:
    output = []
    for array in arrays:
        type_count = len(set([type(item) for item in array]))
        if type_count == 1:
            output.append(array)
    return output


def test() -> None:
    # Expected: [[1, 5, 4], ['b']]
    print(filter_homogenous([[1, 5, 4], ['a', 3, 5], ['b'], [], ['1', 2, 3]],))


if __name__ == "__main__":
    test()
