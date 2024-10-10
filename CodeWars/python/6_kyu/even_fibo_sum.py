# https://www.codewars.com/kata/55688b4e725f41d1e9000065

def even_fib(n):
    previous_num, current_num, output = 0, 1, 0
    for i in range(n - 1):
        temp = current_num
        current_num += previous_num
        previous_num = temp
        if current_num >= n:
            break
        if current_num % 2 == 0:
            output += current_num
    return output


def test():
    # Not part of the actual solution
    test_cases = (0, 2, 8, 33, 25997544)
    for i in range(len(test_cases)):
        print(f"Test Case #{i + 1}: {even_fib(test_cases[i])}")


if __name__ == '__main__':
    test()
