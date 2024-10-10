# https://www.codewars.com/kata/596f72bbe7cd7296d1000029/train/python

def deep_count(a):
    def count_items(arr, index, count):
        if index + 1 >= len(arr):
            return count
        if type(arr[index]) == list:
            return count_items(arr[index], 0, count + 2)
        return count_items(arr, index + 1, count + 1)
    return count_items(a, 0, 0)

# Test code, not part of the solution
def test():
    test_cases = [
        [],                   
        [1, 2, 3],            
        ["x", "y", ["z"]],
        [1, 2, [3, 4, [5]]]
    ]
    for test_case in test_cases:
        print(deep_count(test_case))

if __name__ == "__main__":
    test()