# https://www.codewars.com/kata/5a5915b8d39ec5aa18000030/train/python

def find_missing(arr1: list, arr2: list) -> int:
    for element in arr1:
        if not element in arr2 or arr1.count(element) != arr2.count(element):
            return element
