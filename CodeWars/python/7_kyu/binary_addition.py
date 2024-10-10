# https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/python

def binary_array_to_number(arr: list[int]):
    arr.reverse()
    output = 0
    for i, n in enumerate(arr):
        if i == 0:
            output += n
            continue
        output += n * 2 ** i
    return output


# test code
# print(binary_array_to_number([0, 0, 0, 1]))
print(binary_array_to_number([1, 1, 0, 1]))
# print(binary_array_to_number([1, 1, 1, 1]))
