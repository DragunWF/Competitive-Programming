# ://www.codewars.com/kata/596f72bbe7cd7296d1000029/train/python

def deep_count(arr):
    count = 0

    def traverse(item, index):
        nonlocal count
        if index >= len(item):
            return
        count += 1
        if type(item[index]) is list:
            traverse(item[index], 0)
        traverse(item, index + 1)

    traverse(arr, 0)
    return count


def test():
    # Not part of the solution, just testing
    print(deep_count([1, 2, [3, 4, [5]]]))  # 7
    print(deep_count([[[[[[[[[]]]]]]]]]))  # 8
    print(deep_count([['a'], []]))


if __name__ == '__main__':
    test()
