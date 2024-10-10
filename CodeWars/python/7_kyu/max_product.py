# https://www.codewars.com/kata/5a4138acf28b82aa43000117

def adjacent_element_product(array):
    values, index = [], 0
    for x in array:
        if index != len(array) - 1:
            values.append(x * array[index + 1])
        index += 1
    return max(values)
