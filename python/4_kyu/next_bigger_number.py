from collections import Counter


def next_bigger(n: int) -> int:
    if not validate(n):
        return -1
        
    keys = Counter(str(n))
    while True:
        n += 1
        incremented_keys = Counter(str(n))
        if keys == incremented_keys:
            return n


def validate(n: int) -> bool:
    str_num = str(n)
    if len(set(str_num)) == 1:
        return False
    for i in range(len(str_num) - 1):
        if int(str_num[i]) < int(str_num[i + 1]):
            return True
    return False


test_cases = [12, 513, 2017, 9, 111, 531]
for case in test_cases:
    print(next_bigger(case))

# https://www.codewars.com/kata/55983863da40caa2c900004e/python
