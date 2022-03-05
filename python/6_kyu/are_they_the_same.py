# https://www.codewars.com/kata/550498447451fbbd7600041c

def comp(arr1, arr2):
    if arr1 == [] and arr2 == []: return True
    if not arr1 or not arr2: return False
    arr1 = [x * x for x in arr1]
    arr1.sort(), arr2.sort()
    if arr1 == arr2: return True
    return False
