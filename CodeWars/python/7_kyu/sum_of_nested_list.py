# https://www.codewars.com/kata/5a15a4db06d5b6d33c000018/train/python

def sum_nested(lst):
    def recurse(element):
        total = 0
        if type(element) == list:
            for item in element:
                total += recurse(item) if type(item) == list else item
            return total
        return element
    return recurse(lst)


def test():
    print(sum_nested([1, [2, [3, [4]]]])) # 10


if __name__ == "__main__":
    test()