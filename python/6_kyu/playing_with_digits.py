# https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python

def dig_pow(n: int, p: int) -> int:
    total, str_num = 0, str(n)
    for i in range(len(str_num)):
        total += int(str_num[i]) ** (p + i)
    k = total / n
    return int(k) if k % 1 == 0 else -1


def test():
    # Not part of the solution, just testing
    print(dig_pow(89, 1))
    print(dig_pow(92, 1))
    print(dig_pow(46288, 3))


if __name__ == '__main__':
    test()
