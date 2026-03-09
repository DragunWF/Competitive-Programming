# https://www.codewars.com/kata/699af631058f5c12b04f4efe/train/python

def stalin_sort(arr: list[int]) -> list:
    if not arr:
        return None
    stalin_sorted = [arr[0]]
    prev_element = arr[0]
    for i in range(1, len(arr)):
        if arr[i] >= prev_element:
            stalin_sorted.append(arr[i])
            prev_element = arr[i]
    arr.clear()
    for element in stalin_sorted:
        arr.append(element)
