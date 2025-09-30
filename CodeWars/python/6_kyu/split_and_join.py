# https://www.codewars.com/kata/5816ead8dae5a59eaa000053/train/python

def split(arr: list[int]) -> list[list[int], tuple[list[int]]]:
    flattened = []
    lengths = []
    for sublist in arr:
        lengths.append([len(sublist)])
        for item in sublist:
            flattened.append(item)
    return (flattened, lengths)


def join(arr1: list[list[int]], arr2: list[list[int]]) -> list[list[int]]:
    output = []
    arr1_checkpoint_index = 0
    for item in arr2:
        target_sublist_length = item[0]
        sublist = []
        for i in range(arr1_checkpoint_index, len(arr1)):
            sublist.append(arr1[i])
            if len(sublist) == target_sublist_length:
                arr1_checkpoint_index = i + 1
                break
        output.append(sublist)
    return output


def test() -> None:
    test_case = split([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]])
    print(test_case)
    print(join(test_case[0], test_case[1]))


if __name__ == "__main__":
    test()
