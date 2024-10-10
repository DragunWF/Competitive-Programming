# https://www.codewars.com/kata/5511b2f550906349a70004e1/train/python

def last_digit(a, b):
    if b == 0:
        return 1

    # List of cycles for last digits mod 10. The last digit indicates the index
    cycles = ([0], [1], [2, 4, 8, 6], [3, 9, 7, 1],
              [4, 6], [5], [6], [7, 9, 3, 1],
              [8, 4, 2, 6], [9, 1])

    # Find the cycle for the last digit of 'a'
    last_digit_of_a = a % 10
    cycle = cycles[last_digit_of_a]

    # Calculate which element in the cycle
    cycle_length = len(cycle)
    index = (b % cycle_length) - 1

    # If b is a multiple of the cycle length, we take the last element of the cycle
    return cycle[index]


def test():
    # Not part of the solution, just testing
    print(last_digit(9, 7))
    print(last_digit(10, 10 ** 10))
    print(last_digit(33, 5))


if __name__ == '__main__':
    test()
