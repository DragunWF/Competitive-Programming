# https://www.codewars.com/kata/5609fd5b44e602b2ff00003a/train/python

def process_2arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    set_a, set_b = set(arr1), set(arr2)
    common_elements_count = len(set_a.intersection(set_b))
    unique_elements = len(arr1) + len(arr2) - common_elements_count * 2
    set_a_diff_count = len(set_a.difference(set_b))
    set_b_diff_count = len(set_b.difference(set_a))
    return [common_elements_count, unique_elements, set_a_diff_count, set_b_diff_count]
