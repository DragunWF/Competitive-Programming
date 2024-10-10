# https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004/python

def highest_rank(arr: list):
    max_count = 0
    highest = None
    for element in set(arr):
        count = arr.count(element)
        if count > max_count or count == max_count and element > highest:
            max_count = count
            highest = element
    return highest

# Test code, this is not part of the solution
def test():
    print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12, 10]))

if __name__ == "__main__":
    test()