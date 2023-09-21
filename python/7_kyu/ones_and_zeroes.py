# https://www.codewars.com/kata/650a86e8404241005fc744ca/train/python

def to_consecutive(txt, separator):
    binary_list = txt.split(separator)
    if binary_list[0] and binary_list[0][0] == "0":
        return -1
    return ["1" * len(i) for i in binary_list if i]


def same_length(txt):
    return to_consecutive(txt, "0") == to_consecutive(txt, "1")


def test():
    # Not part of the solution
    test_cases = ("110011100010", "101010110", "00110100001111")
    for i in range(len(test_cases)):
        result = same_length(test_cases[i])
        print(f"Test Case #{i + 1}: {result}")


if __name__ == "__main__":
    test()
